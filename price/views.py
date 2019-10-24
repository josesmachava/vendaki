from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, View

from dashboard.models import *
from dashboard.models import *


# Create your views here.


def index(request):
    social_media = SocialMedia.objects.all()
    categories = Category.objects.filter(type="empresa")
    companies =  Company.objects.all()
    try:
        order = Order.objects.get(user=request.user, ordered=False)
        return render(request, 'index.html', {'social_media': social_media, 'order': order, 'categories': categories, 'companies': companies})
    except Order.DoesNotExist:

        return render(request, 'index.html', {'social_media': social_media, 'categories': categories, 'companies': companies})


def products(request):
    categories = Category.objects.filter(type="produto")
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products, 'categories': categories})




def products(request, id):
    categories = Category.objects.filter(type="produto")
    products = Product.objects.filter(company_id=id)
    return render(request, 'products.html', {'products': products, 'categories': categories})



def dashboard(request):
    return render(request, 'dashboard.html')


def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    order_product, created = OrderProduct.objects.get_or_create(product=product, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.product.filter(product_id=product.id).exists():
            order_product.quantity += 1
            order_product.save()
            messages.info(request, "A quatidade do producto foi alterada")
        else:
            messages.info(request, "Produto addicionado no carinho")
            order.product.add(order_product)

    else:
        order = Order.objects.create(user=request.user)
        order.product.add(order_product)
        messages.info(request, "Produto addicionado no carinho")
    return redirect('products')


class OrderSummary(View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'order_summary.html', context)

        except ObjectDoesNotExist:
            messages.error(self.request, "You do not hava an active order")
            return redirect('products')


def remove_from_cart(request, id):
    product = get_object_or_404(Product, id=id)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.product.filter(product_id=product.id).exists():
            order_product = OrderProduct.objects.filter(product=product, user=request.user, ordered=False)[0]
            order.product.remove(order_product)
            messages.info(request, "o produto foi removido do seu carinho")

        else:
            messages.info(request, "este producto nao esta no seu carinho")
            return redirect('products')
    else:
        messages.info(request, "o usuario nao tem uma encomenda")
        return redirect('products')
    return redirect('products')


def handler404(request, exception):
    return render(request, 'error404.html', status=404)


def handler500(request):
    return render(request, 'error500.html', status=500)
