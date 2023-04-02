from http import HTTPStatus

import json
from base64 import b64encode, b64decode

import requests
import secrets

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5


def create_bearer_token(public_key, api_key):
    key_der = b64decode(public_key)
    key_pub = RSA.importKey(key_der)
    cipher = Cipher_PKCS1_v1_5.new(key_pub)
    cipher_text = cipher.encrypt(api_key.encode('ascii'))
    encrypted_msg = b64encode(cipher_text)

    return encrypted_msg


public_key = " MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAyrOP7fgXIJgJyp6nP/Vtlu8kW94Qu+gJjfMaTNOSd/mQJChqXiMWsZPH8uOoZGeR/9m7Y8vAU83D96usXUaKoDYiVmxoMBkfmw8DJAtHHt/8LWDdoAS/kpXyZJ5dt19Pv+rTApcjg7AoGczT+yIU7xp4Ku23EqQz70V5Rud+Qgerf6So28Pt3qZ9hxgUA6lgF7OjoYOIAKPqg07pHp2eOp4P6oQW8oXsS+cQkaPVo3nM1f+fctFGQtgLJ0y5VG61ZiWWWFMOjYFkBSbNOyJpQVcMKPcfdDRKq+9r5DFLtFGztPYIAovBm3a1Q6XYDkGYZWtnD8mDJxgEiHWCzog0wZqJtfNREnLf1g2ZOanTDcrEFzsnP2MQwIatV8M6q/fYrh5WejlNm4ujnKUVbnPMYH0wcbXQifSDhg2jcnRLHh9CF9iabkxAzjbYkaG1qa4zG+bCidLCRe0cEQvt0+/lQ40yESvpWF60omTy1dLSd10gl2//0v4IMjLMn9tgxhPp9c+C2Aw7x2Yjx3GquSYhU6IL41lrURwDuCQpg3F30QwIHgy1D8xIfQzno3XywiiUvoq4YfCkN9WiyKz0btD6ZX02RRK6DrXTFefeKjWf0RHREHlfwkhesZ4X168Lxe9iCWjP2d0xUB+lr10835ZUpYYIr4Gon9NTjkoOGwFyS5ECAwEAAQ=="
api_key = "q6phoogrb6feqthw6fco8i5iz2lrwipy"

print(create_bearer_token(public_key, api_key))

api_context_address = 'api.vm.co.mz'

x = 'input_ServiceProviderCode', '900511'


def sandbox_create_mpesa_payment(amount, msisdn):
    payment_body = {
        "input_TransactionReference": "T12344C",
        "input_CustomerMSISDN": "258" + msisdn,
        "input_Amount": amount,
        "input_ThirdPartyReference": secrets.token_hex(6),
        "input_ServiceProviderCode": "171717"

    }
    headers = {
        "Authorization": "Bearer P3qODOlTB9Sb4h8WhFRAx9NEMV1sz199n8H7Hznn/GwPd/6P5gA4RmRVukXNYh4uO6S4hnrgCkQ3Q2aO5nzbf9673gHmwUqvYBxLUskx0ciai7khQ0IGIyoA5PPau2RYZIMFi6qlEsJVW1KVAzumByk+kFIwsG3U8IvY9p784pnEfl+Jo6B1CUQn+N56c4Zam21gybNZ00RfLeio9fydhFCr48qFREsuo6jGMK16S1FdOOJP+MoGfsozDTob/5Y3nvaMFJn2KKCNtOq5M0ptV7HPlcyWNLkJ+XPaqvHqgnVpnQ43w88nbQOPA14f/RP8g3Yt0G8iE3Ziya9RqQu8CRbZaLJXqHUizyl9JcNr6ZpGUeFyJ6Wdmzm2hyrjOFXUa/rCrO7GDIvFkg/OEtdQPkWf4UxMg/h4rZ9qDn4/5tD63uugsfbPOln/qrtG6nVPNbY0OMwB9qPjbCIUzzXjvHLl/vpc0553YddPOx9XvPd5sc6au8biPPXkP5GZT2lnJBAIMJ9YvnHJQqmSZnbfYIwBaEY2qskKCqCCsX5X0pWUtHFTC42cRJJN8UwU6Zb4W3TauS0H5/mBzuku6e9lprgaw21ex1bkxYTzPa0j+jjug/hmhQXc4u6WuSoU80Lp6EBq0QtbzokOVMlYZ5iPZCjA1EdEiB95qX2UVTmSYLc=",
        "Content-Type": "application/json",
        "Origin": '*',
        "Host": "api.sandbox.vm.co.mz"

    }

    make_payment = requests.post("https://api.vm.co.mz:18352/ipg/v1x/c2bPayment/singleStage/",
                                 data=json.dumps(payment_body),
                                 headers=headers)
    print(make_payment.status_code)
    print(make_payment.json())
    out = make_payment.json()
    # print(out["output_ResponseCode"])

    return out


def create_mpesa_payment(amount, msisdn):
    payment_body = {
        "input_TransactionReference": "T12344C",
        "input_CustomerMSISDN": "258" + msisdn,
        "input_Amount": amount,
        "input_ThirdPartyReference": secrets.token_hex(6),
        "input_ServiceProviderCode": "900511"

    }
    headers = {
        "Authorization": "Bearer SbTluzd8eXHTd8skgIkJgxQAE66LCtG5u3CQMCpmvlTkzIycBgIhJHmu8hrRybBjs4tu76+SqRMMfezpI/QtZgamsEibz45D8ty+U10FmO2Mc07J3ZLPs//3kds9cKLP8Fk0ls1kpDxfk/sDcV/qW/JxQ81+kShNCUBSAvJgXPwrjfhh3wVqjSPIdWKqxqdUFdjXrv8H1BNPLOsfcFvkW9jgl6h015Cjme2GliQOUpA/bbijZXGA4RMlGlKVoj0GMfxQ6QjjnH1zzOzO8p23hXaXUq5vBvAcYUWCrhDVfJ77w3fSKRZfJAvWTraii5sEKSioXJfYuYpiIkJ/U7TUEYQmXgSykjyw0ILgcCRp39wRQRBfSl5lHHNsvUklz+Y5KJoop3sHij7mHzRIQOJOi8+cb951i8pcFMlLHZ/fKkR0XCEgUJOyz/mJ/zWWEzdqEv1ahcx4NjyLfg4/dby8eNsBGVPaSPyzsg+K8RhnOgt4N4gX6ILtBvnwdsznlXEZbJ6IDRvz02t3w5jMCt7fN+kcgqt5jiNLiNSTNlSknTPRYm0UsL0HuBQXfgnZaojVKCocgXZH/UpJNfcawyPm98ZVAG3XV+apq3dV4z3M6xBAZOvsdkLjfXArfw3GF/iVdUuYpRJcNdl8hQ7u+OpwcQq5SfWggLFfHxsj+oqzmDk=",
        "Content-Type": "application/json",
        "Origin": '*',
        "Host": "api.vm.co.mz"

    }

    make_payment = requests.post("https://api.vm.co.mz:18352/ipg/v1x/c2bPayment/singleStage/",
                                 data=json.dumps(payment_body),
                                 headers=headers)
    print(make_payment.status_code)
    print(make_payment.json())
    out = make_payment.json()
    print(out["output_ResponseCode"])

    return make_payment



