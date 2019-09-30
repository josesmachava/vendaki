from django.shortcuts import render
from dashboard.models import *
# Create your views here.


def index(request):
    social_media = SocialMedia.objects.all()
    return render(request, 'index.html', {'social_media': social_media})



def dashboard(request):
    return render(request, 'dashboard.html')


