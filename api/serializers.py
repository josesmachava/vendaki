from rest_framework import serializers
from dashboard.models import *


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class OrderProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderProduct
        fields = ['id', 'product']




class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number']


class OrderSerializer(serializers.ModelSerializer):
    product = OrderProductSerializer(read_only=True, many=True)

    user = UserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'qrcode_image', 'user', 'product']
