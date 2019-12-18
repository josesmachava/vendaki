import random
import string

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import View, DeleteView, DetailView
from pinax.referrals.models import Referral

from account.models import ReferralLink
from dashboard.models import *


# Create your views here.


def index(request):
    social_media = SocialMedia.objects.all()
    categories = Category.objects.filter(type_id=1)
    companies = Company.objects.all()
    if not request.user.is_authenticated:
        return render(request, 'index.html',
                      {'social_media': social_media, 'categories': categories, 'companies': companies})

    try:

        order = Order.objects.get(user=request.user, ordered=False)

        return render(request, 'index.html',
                      {'social_media': social_media, 'order': order, 'categories': categories, 'companies': companies})
    except Order.DoesNotExist:

        return render(request, 'index.html',
                      {'social_media': social_media, 'categories': categories, 'companies': companies})


def products(request):
    categories = Category.objects.filter(type_id=2)
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products, 'categories': categories})


def products(request, id):
    categories = Category.objects.filter(type_id=1)
    products = Product.objects.filter(company_id=id)
    return render(request, 'products.html', {'products': products, 'categories': categories})


def product(request):
    categories = Category.objects.filter(type_id=2)
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products, 'categories': categories})


def dashboard(request):
    return render(request, 'dashboard.html')


@method_decorator(login_required, name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


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
    return redirect('product')


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
            return redirect('product')





class RefereLink(View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'referral.html', context)

        except ObjectDoesNotExist:
            messages.error(self.request, "You do not hava an active order")
            return redirect('product')


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
            return redirect('product')
    else:
        messages.info(request, "o usuario nao tem uma encomenda")
        return redirect('product')
    return redirect('product')


def show_links(request):
    order = Order.objects.get(user=request.user, ordered=False)
    referral_links = ReferralLink.objects.filter(user=request.user)
    print(order.product.all())
    for orders in order.product.all():
        print(orders.product.id)
        referral_link, created = ReferralLink.objects.get_or_create(user=request.user,
                                                                    link=f'www.preco.co.mz/product/{request.user.referral.referral_token}/{orders.product.id}',
                                                                    name=orders.product.name,
                                                                    referral=request.user.referral.referral_token)

    order.ordered = True
    order.save()
    return render(request, 'referral.html', {'referral_link': referral_links})


def handler404(request, exception):
    return render(request, 'error404.html', status=404)


def handler500(request):
    return render(request, 'error500.html', status=500)
