import os

from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.views.static import serve

from payment.forms import PaymentForm
from payment.models import Payment
from .forms import ProductForm
from .models import Product, Order, OrderProduct
import requests
import json
# Create your views here.
from account.models import User, Store


def index(request):
    return render(request, "dashboard/index.jade")


# @method_decorator(login_required, name='dispatch')
class ProductCreateView(CreateView):
    form_class = ProductForm

    template_name = 'dashboard/product/create.jade'
    success_url = reverse_lazy('product-list')

    def form_valid(self, form):
        print(form)
        form.instance.user = self.request.user
        print(form.instance.user)
        return super().form_valid(form)


class ProductListView(ListView):
    model = Product
    template_name = 'dashboard/product/list.jade'
    context_object_name = 'products'
    paginate_by = 13

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        products = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(products, self.paginate_by)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        context['product'] = products
        return context


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'dashboard/product/update.jade'
    context_object_name = 'product'
    fields = ('name', 'description', 'price', 'discount', 'categories', 'company')

    def get_success_url(self):
        return reverse_lazy('product-list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'dashboard/product/delete.html'
    success_url = reverse_lazy('product-list')


class OrdertListView(ListView):
    model = Order
    template_name = 'dashboard/order/list.jade'
    context_object_name = 'order'
    paginate_by = 11

    def get_context_data(self, **kwargs):
        context = super(OrdertListView, self).get_context_data(**kwargs)
        orders = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(orders, self.paginate_by)
        try:
            orders = paginator.page(page)
        except PageNotAnInteger:
            orders = paginator.page(1)
        except EmptyPage:
            orders = paginator.page(paginator.num_pages)
        context['order'] = orders
        return context


class UserListView(ListView):
    model = User
    template_name = 'dashboard/user/list.jade'
    context_object_name = 'users'
    paginate_by = 13

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        users = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(users, self.paginate_by)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        context['users'] = users
        return context


class UserUpdateView(UpdateView):
    model = User
    template_name = 'dashboard/user/update.html'
    context_object_name = 'user'
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy('user-list', kwargs={'pk': self.object.id})


class UserDeleteView(DeleteView):
    model = User
    template_name = 'dashboard/user/delete.html'
    success_url = reverse_lazy('user-list')


def store(request, slug, slug_product):
    stores = Store.objects.get(slug=slug)
    product = Product.objects.get(store=stores, slug=slug_product)
    if request.method == "POST":

        form = PaymentForm(request.POST)
        if form.is_valid():
            order_product, created = OrderProduct.objects.get_or_create(store=stores, product=product, ordered=False)
            order, created = Order.objects.get_or_create(store=stores,  ordered=False)
            order.save()
            order.product.add(order_product)
            payment = form.save(commit=False)
            payment.name = request.POST.get('name')
            payment.número_de_telefone = request.POST.get('número_de_telefone')
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
                order.ordered = True
                order_product.save()
                order.save()
                payment.status_code = status_code
                payment.save()
                redirect('download', payment.número_de_telefone, product.id)

            else:
                error_message = response['transaction_status']

                messages.error(request, error_message)

                form = PaymentForm()

        #  return redirect('post_detail', pk=post.pk)
    else:
        form = PaymentForm()

    return render(request, 'dashboard/store/index.jade', {'product': product, 'form': form, })


def download(request, number, pk):
    payment = Payment.objects.get(número_de_telefone=number, order__product=pk, status_code="201")
    payment_id = payment.order.id
    order = OrderProduct.objects.get(id=payment_id, ordered=True)
    product = order.product

    return  render(request, 'dashboard/store/download.jade', {"product":product})