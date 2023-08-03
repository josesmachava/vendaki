"""price URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
       path("painel/", login_required(views.index), name="dashboard"),
   path("user/", login_required(views.UserListView.as_view()), name="user-list"),
   path('user/<int:pk>/update', login_required(views.UserUpdateView.as_view()),
         name='user-update'),
   path('user/<int:pk>/delete', login_required(views.UserDeleteView.as_view()),
         name='user-delete'),
   path("order/", login_required(views.PaymentListView.as_view()), name="order"),
   path('product/create', login_required(views.ProductCreateView.as_view()),
        name='create-product'),
    path('product/<int:pk>/update', login_required(views.ProductUpdateView.as_view()),
         name='product-update'),
    path('product/<int:pk>/delete', login_required(views.ProductDeleteView.as_view()),
         name='product-delete'),
   path('product/list', login_required(views.ProductListView.as_view()),
        name='product-list'),
   path('s3direct/', include('s3direct.urls')),


   
]
