
from django.urls import path, include
from . import views

urlpatterns = [

    path('download/<int:number>/<int:pk>/', views.download   , name='download'),

]
