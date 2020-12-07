from django.contrib import messages
from django.shortcuts import render, redirect
import requests
import json
# Create your views here.
from account.models import Store
from dashboard.models import OrderProduct, Product, Order
from payment.forms import PaymentForm














def index(request, slug):
    store = Store.objects.get(slug=slug)
    products = Product.objects.filter(store=store)

    return render(request, 'store/index.jade', {'products': products, 'store': store})


def store(request, slug, slug_product):
    store = Store.objects.get(slug=slug)
    product = Product.objects.get(store=store, slug=slug_product)
    if request.method == "POST":

        form = PaymentForm(request.POST)
        if form.is_valid():

            order_product, created = OrderProduct.objects.get_or_create(store=store, product=product, ordered=False)
            order, created = Order.objects.get_or_create(store=store, ordered=False)
            order.save()
            name = request.POST.get('name')
            número_de_telefone = request.POST.get('número_de_telefone')
            order.product.add(order_product)
            payment = form.save(commit=False)
            payment.name = name
            payment.número_de_telefone = número_de_telefone
            payment.order = order

            API_ENDPOINT = "https://development-xindiri.herokuapp.com/v1/payments/"
            data = {

                'phone_number': payment.número_de_telefone,
                'amount': product.price,
                'api_key': 'a0a9fe0bf9178657835ab0ad4b033f9f',

            }

            payment_data = requests.post(url=API_ENDPOINT, data=data)
            print(payment_data)
            response = json.loads(payment_data.text)

            status_code = response["transaction_status_code"]

            if status_code == 201 or status_code == 200:

                order_product.ordered = True
                order_product.name = name
                order_product.número_de_telefone = número_de_telefone
                order_product.save()
                order.name = name
                order.número_de_telefone = número_de_telefone
                order.ordered = True
                order.save()
                payment.status_code = status_code
                payment.save()
                return redirect('download', payment.número_de_telefone, product.id)

            else:
                error_message = response['transaction_status']
                order_product.name = name
                order_product.número_de_telefone = número_de_telefone

                order_product.save()

                order.name = name
                order.número_de_telefone = número_de_telefone
                order.save()
                payment.status_code = status_code
                payment.save()
                messages.error(request, error_message)
                form = PaymentForm()

        #  return redirect('post_detail', pk=post.pk)
    else:
        form = PaymentForm()

    return render(request, 'store/product.jade', {'product': product, 'form': form, 'store': store})




def download(request, number, pk):
    payment = OrderProduct.objects.get(número_de_telefone=number, product=pk, ordered=True)
    product = Product.objects.get(pk=payment.product.pk)

    return render(request, 'store/download.jade', {"product": product})
