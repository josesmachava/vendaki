from django.shortcuts import render
from django.shortcuts import render
import json
import requests
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from dashboard.models import Company, Order


# Create your views here.
@api_view(['GET', 'POST'])
def Companies(request):
    """
    List all code Payment, or create a new Payment.
    """
    if request.method == 'GET':
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response(serializer.data)


    #Get Data from Post API




@api_view(['GET', 'POST'])
def APIOrders(request):
    """
    List all code Payment, or create a new Payment.
    """
    if request.method == 'GET':
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)


    #Get Data from Post API

@api_view(['GET', 'POST'])
def APIOrder(request, id):
    """
    List all code Payment, or create a new Payment.
    """
    if request.method == 'GET':
        order = Order.objects.filter(id=id)
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)
