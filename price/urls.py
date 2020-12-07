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
from django.conf.urls.static import static # new
    
from price import settings
from . import views
from store.views import store
from django.conf.urls import handler404, handler500, url

urlpatterns = [
    path('account/', include("account.urls")),
    path('about/', include("about.urls")),
    path('admin/', admin.site.urls),
    url(r'^s3direct/', include('s3direct.urls')),
    path('tinymce/', include('tinymce.urls')),

    path('<str:slug>/<str:slug_product>', store, name="store"),
    path("", views.index, name="index"),
    path("dashboard/", include("dashboard.urls")),

]




handler404 = "price.views.handler404"
handler500 = "price.views.handler500"



if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)