from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .models import Products

# Create your views here.
from account.models import Company


def index(request):
    return render(request, "dashboard/index.html")


def painel(request):
    return render(request, "dashboard/painel.html")


def user(request):
    return render(request, "dashboard/user.html")



def order(request):
    return render(request, "dashboard/order.html")


class ProductListView(ListView):
    model = Products
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


# @method_decorator(login_required, name='dispatch')
class ProductCreateView(CreateView):
    model = Products
    template_name = 'dashboard/product/create.html'
    fields = ('name', 'description', 'price', 'discount', 'category', 'company')
    success_url = reverse_lazy('product-list')


def companies(request):
    companies = Company.objects.all()
    return render(request, "dashboard/companies.html", {'companies': companies})


def editar_empresas(request):
    return render(request, "dashboard/editar_empresa.html")
