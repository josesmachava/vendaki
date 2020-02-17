import random
import string

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.utils.decorators import method_decorator
from django.views.generic import View, DeleteView, DetailView, ListView

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

def categories(request, id):
    social_media = SocialMedia.objects.all()
    categories = Category.objects.filter(type_id=1)
    companies = Company.objects.filter(categories=id)

    if not request.user.is_authenticated:
        return render(request, 'companies.html'
                               ,
                      {'social_media': social_media, 'categories': categories, 'companies': companies})

    try:

        order = Order.objects.get(user=request.user, ordered=False)

        return render(request, 'companies.html',
                      {'social_media': social_media, 'order': order, 'categories': categories, 'companies': companies})
    except Order.DoesNotExist:

        return render(request, 'companies.html',
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


def search(request):
    return render(request, 'price/search.html')


def dashboard(request):
    return render(request, 'dashboard.html')


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


def add_to_cart_referral(request, id, referral):
    product = get_object_or_404(Product, id=id)
    order_product, created = OrderProduct.objects.get_or_create(product=product, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    print("hello")
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
    referred_link = ReferredLink.objects.create(user=request.user,
                                                link=f'www.preco.co.mz/product/{referral}/{id}',
                                                product=product,
                                                referral=referral)

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


def create_referral(request):
    order = Order.objects.get(user=request.user, ordered=False)
    referral_links = ReferralLink.objects.filter(user=request.user)
    print(order.product.all())
    for orders in order.product.all():
        print(orders.product.id)
        referral_link, created = ReferralLink.objects.get_or_create(user=request.user,
                                                                    link=f'www.preco.co.mz/product/{request.user.referral.referral_token}/{orders.product.id}',
                                                                    product=orders.product,
                                                                    referral=request.user.referral.referral_token)

    order.ordered = True
    order.save()
    return render(request, 'referral.html', {'referral_link': referral_links})


class ReferralLinkListView(ListView):
    model = ReferralLink
    template_name = 'referral/list.html'
    context_object_name = 'referrals'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ReferralLinkListView, self).get_context_data(**kwargs)
        referrals = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(referrals, self.paginate_by)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        context['referrals'] = referrals
        return context


def referrallist(request):
    referral_links = ReferralLink.objects.filter(user=request.user.pk)
    return render(request, 'referral/list.html', {'referral_link': referral_links})



def handler404(request, exception):
    return render(request, 'error/404.jade', status=404)

def handler500(request):
    return render(request, 'error/500.html', status=500)