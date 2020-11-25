from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from payment.forms import PaymentForm
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


def store(request, slug):
    stores = Store.objects.get(slug=slug)
    print(stores)
    products = Product.objects.filter(store=stores)
    print(products)
    if request.method == "POST":

        form = PaymentForm(request.POST)
        if form.is_valid():
            order_product, created = OrderProduct.objects.get_or_create(store=store, product=products, ordered=False)
            order, created = Order.objects.get_or_create(store=store, product=order_product, ordered=False)
            payment = form.save(commit=False)
            payment.name = request.POST.get('name')
            payment.número_de_telefone = request.POST.get('número_de_telefone')
            payment.order = order

            API_ENDPOINT = "https://development-xindiri.herokuapp.com/v1/payments/"
            data = {

                'phone_number': payment.número_de_telefone,
                'amount': request.POST.get('price'),
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

                payment.save()

            else:
                error_message = data['transaction_status']

                messages.error(request, error_message)

                form = PaymentForm()

        #  return redirect('post_detail', pk=post.pk)
    else:
        form = PaymentForm()

    return render(request, 'dashboard/store/index.jade', {'products': products, 'form': form, })


def stores(request, slug):
    try:
        store = Store.objects.get(slug=str(slug))
    except Store.DoesNotExist:
        store = None
    print(slug)
    print(store)

    products = Product.objects.filter(store=store)

    if request.method == "POST":

        form = PaymentForm(request.POST)
        if form.is_valid():
            order_product, created = OrderProduct.objects.get_or_create(store=store, product=products, ordered=False)
            order, created = Order.objects.get_or_create(store=store, product=order_product, ordered=False)

            payment = form.save(commit=False)
            payment.name = request.POST.get('name')
            payment.número_de_telefone = request.POST.get('número_de_telefone')
            payment.order = order

            API_ENDPOINT = "https://development-xindiri.herokuapp.com/v1/payments/"
            data = {

                'phone_number': payment.número_de_telefone,
                'amount': products.price,
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

                payment.save()

                return redirect('thanks')

            else:
                order_product.save()
                order.save()
                error_message = data['transaction_status']

                messages.error(request, error_message)

                form = PaymentForm()

        #  return redirect('post_detail', pk=post.pk)
    else:
        form = PaymentForm()

    return render(request, 'dashboard/store/index.jade', {'products': products, 'form': form, })
