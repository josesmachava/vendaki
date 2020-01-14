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

urlpatterns = [
   path("", views.index, name="dashboard"),
   path("painel/", views.painel, name="painel"), 
   path("companies/", views.CompanyListView.as_view(), name="companies"),
   path("user/", views.UserListView.as_view(), name="user-list"),
   path('user/<int:pk>/update', views.UserUpdateView.as_view(),
         name='user-update'),
   path('user/<int:pk>/delete', views.UserDeleteView.as_view(),
         name='user-delete'),
   path("order/", views.OrdertListView.as_view(), name="order"),
   path('product/create', views.ProductCreateView.as_view(),
        name='product-create'),
    path('product/<int:pk>/update', views.ProductUpdateView.as_view(),
         name='product-update'),
    path('product/<int:pk>/delete', views.ProductDeleteView.as_view(),
         name='product-delete'),
   path('product/list', views.ProductListView.as_view(),
        name='product-list'),
   path("editar_empresas/", views.editar_empresas, name="editar_empresas"),
   path('order/<int:pk>', views.OrderDetailView.as_view(),
                       name='order-detail'),
   path('complete/<int:order_pk>/<int:user_pk>', views.complete_order,
                       name='complete-order'),

   
]
