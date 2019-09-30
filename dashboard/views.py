from django.shortcuts import render, redirect, HttpResponse

# Create your views here.



def index( request):
    return render(request, "dashboard/index.html")




def painel( request):
    return render(request, "dashboard/painel.html")