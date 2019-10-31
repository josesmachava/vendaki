from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from .models import Product, Order

# Create your views here.
from account.models import Company, User


def index(request):
    company = Company.objects.all().count()
    product = Product.objects.all().count()
    order   = Order.objects.all().count()
    return render(request, "dashboard/index.html", {'product':product, 'company':company, 'order':order})


def painel(request):
    return render(request, "dashboard/painel.html")









# @method_decorator(login_required, name='dispatch')
class ProductCreateView(CreateView):
    model = Product
    template_name = 'dashboard/product/create.html'
    fields = ('name', 'description', 'price', 'discount', 'categories', 'company', 'type', "number")
    success_url = reverse_lazy('product-list')


class ProductListView(ListView):
    model = Product
    template_name = 'dashboard/product/list.html'
    context_object_name = 'products'
    paginate_by = 5

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
    template_name = 'dashboard/product/update.html'
    context_object_name = 'product'
    fields = ('name', 'description', 'price', 'discount', 'categories', 'company')


    def get_success_url(self):
            return reverse_lazy('product-list', kwargs={'pk': self.object.id})




class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'dashboard/product/delete.html'
    success_url = reverse_lazy('product-list')


class OrdertListView(ListView):
    model = Order
    template_name = 'dashboard/product/order.html'
    context_object_name = 'orders'
    paginate_by = 5

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
    template_name = 'dashboard/user/list.html'
    context_object_name = 'users'
    paginate_by = 20

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



class CompanyListView(ListView):
    model = Company
    template_name = 'dashboard/companies.html'
    context_object_name = 'companies'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(CompanyListView, self).get_context_data(**kwargs)
        companies = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(companies, self.paginate_by)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        context['companies'] = companies
        return context



def companies(request):
    companies = Company.objects.all()
    return render(request, "dashboard/companies.html", {'companies': companies})


def editar_empresas(request):
    return render(request, "dashboard/editar_empresa.html")
