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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from price import settings
from . import views
from django.conf.urls import handler404, handler500, url

urlpatterns = [
    path('account/', include("account.urls")),
    path('about/', include("about.urls")),
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("products/<int:id>", views.products, name="products"),
    path("product/", views.product, name="product"),
    path("showlinks/", views.create_referral, name="showlinks"),
    path("dashboard/", include("dashboard.urls")),
    path('add_to_cart/<int:id>', views.add_to_cart, name="add_to_cart"),
    path('add_to_cart_referral/<int:id>/<str:referral>/', views.add_to_cart_referral, name="add_to_cart_referral"),
    path('product/<str:referral>/<int:pk>', views.ProductDetailView.as_view(),
         name='product-detail'),
    path("referrals/", views.referrallist, name="referrals"),

                  path('remove_from_cart/<int:id>', views.remove_from_cart, name="remove_from_cart"),
    path('order_summary', views.OrderSummary.as_view(),
         name='order-summary'),
    path('referallink', views.RefereLink.as_view(),
                       name='referallink'),
    path('search',  views.search, name="search")


]




