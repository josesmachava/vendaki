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
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('signin', views.signin, name="signin"),
    path("signup", views.signup, name="signup"),
    path("confirm", views.confirm, name="confirm"),
    path("logout", views.logout_view, name="logout"),
    path('update/<pk>', login_required(views.UserUpdateView.as_view()), name="update-user"),
    path("profile", login_required(views.profile), name="profile"),
    path('', include('django.contrib.auth.urls')),


]
