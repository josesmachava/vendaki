from django.forms import ModelForm
from django import forms
from dashboard.models import Product, Order
from s3direct.widgets import S3DirectWidget
from tinymce.widgets import TinyMCE

class ProductForm(ModelForm):
    name = forms.CharField(max_length=30, label='Nome', required=True,
                                   widget=forms.TextInput(attrs={'placeholder': 'Nome'}))
    price = forms.CharField(max_length=30, label='Preço', required=True,
                                   widget=forms.TextInput(attrs={'placeholder': 'Preço'}))
    description = forms.CharField(label="descrição do producto ", widget=TinyMCE(attrs={}))
    image = forms.URLField(widget=S3DirectWidget(dest='pdf'))

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'image', 'file')