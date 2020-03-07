
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [

    path('companies', views.Companies, name='companies'),
    path('order', views.Orders, name='order'),


]