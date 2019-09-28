from django.shortcuts import render

# Create your views here.



def index(self, request):
    return render(request, "index.html")