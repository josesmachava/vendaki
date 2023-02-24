
from django.urls import path, include

from api.router import api
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    path('download/<int:number>/<int:pk>/', views.download   , name='download'),
    path('create', login_required(views.StoreCreateView.as_view()),
        name='store-create'),
    path('update/<pk>', login_required(views.StoreUpdateView.as_view()), name="update-store"),
    path('update-name/<pk>', login_required(views.StoreUpdateNameView.as_view()), name="update-store-name"),

]

