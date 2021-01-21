
from django.urls import path, include
from . import views

urlpatterns = [

    path('download/<int:number>/<int:pk>/', views.download   , name='download'),
    path('create', views.StoreCreateView.as_view(),
        name='store-create'),
    path('update/<pk>', views.StoreUpdateView.as_view(), name="update-store"),
    path('update-name/<pk>', views.StoreUpdateNameView.as_view(), name="update-store-name"),
    

]

