from django.shortcuts import render

from .forms import PaymentForm
from .models import  Order
from account.models import  Creator
# Create your views here.
from .models import Donation


def purchase(request, pk):
    donation = Donation.objects.get(user_id=pk)
    creator = Creator.objects.get(user_id=pk)

    if request.method == "POST":

        form = PaymentForm(request.POST)
        if form.is_valid():
            order, created = Order.objects.get_or_create(user=creator.user, ordered=False, donation=donation)
            payment = form.save(commit=False)
            payment.name = request.name
            payment.order = order

            API_ENDPOINT = "https://xpayy.herokuapp.com/payment/"
            data = {

                'contact': payment.número_de_telefone,
                'amount': donation.price,
                'reference': secrets.token_hex(6),
                'api_key': '9njrbcqty9ew3cyx4s6k7jvtab134rr6',
                'public_key': '"MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAmptSWqV7cGUUJJhUBxsMLonux24u+FoTlrb+4Kgc6092JIszmI1QUoMohaDDXSVueXx6IXwYGsjjWY32HGXj1iQhkALXfObJ4DqXn5h6E8y5/xQYNAyd5bpN5Z8r892B6toGzZQVB7qtebH4apDjmvTi5FGZVjVYxalyyQkj4uQbbRQjgCkubSi45Xl4CGtLqZztsKssWz3mcKncgTnq3DHGYYEYiKq0xIj100LGbnvNz20Sgqmw/cH+Bua4GJsWYLEqf/h/yiMgiBbxFxsnwZl0im5vXDlwKPw+QnO2fscDhxZFAwV06bgG0oEoWm9FnjMsfvwm0rUNYFlZ+TOtCEhmhtFp+Tsx9jPCuOd5h2emGdSKD8A6jtwhNa7oQ8RtLEEqwAn44orENa1ibOkxMiiiFpmmJkwgZPOG/zMCjXIrrhDWTDUOZaPx/lEQoInJoE2i43VN/HTGCCw8dKQAwg0jsEXau5ixD0GUothqvuX3B9taoeoFAIvUPEq35YulprMM7ThdKodSHvhnwKG82dCsodRwY428kg2xM/UjiTENog4B6zzZfPhMxFlOSFX4MnrqkAS+8Jamhy1GgoHkEMrsT5+/ofjCx0HjKbT5NuA2V/lmzgJLl3jIERadLzuTYnKGWxVJcGLkWXlEPYLbiaKzbJb2sYxt+Kt5OxQqC1MCAwEAAQ==',
            }
            # sending post request and saving response as response object
            r = requests.post(url=API_ENDPOINT, data=data)
            pastebin_url = r.text
            print(pastebin_url, 846244186, movie.price)
            payment.save()
            return redirect('watch', pk)
        #  return redirect('post_detail', pk=post.pk)
    else:
        form = PaymentForm()

    return render(request, 'bossie/purchase.html', {'movie': movie, 'form': form})
