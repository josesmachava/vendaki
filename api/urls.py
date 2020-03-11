
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [

    path('companies', views.Companies, name='companies'),
    path('order', views.APIOrders, name='apiorders'),
    path('order/<int:id>',  views.APIOrder, name='apiorder'),


]