from django.shortcuts import render, redirect, HttpResponse

# Create your views here.



def index( request):
    return render(request, "dashboard/index.html")




def painel( request):
    return render(request, "dashboard/painel.html")


def productos( request):
    return render(request, "dashboard/productos.html")


def empresas( request):
    return render(request, "dashboard/empresas.html")

def editar_empresas( request):
    return render(request, "dashboard/editar_empresa.html")

