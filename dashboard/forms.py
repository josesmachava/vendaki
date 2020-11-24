from django.forms import ModelForm
from django import forms
from dashboard.models import Product
from s3direct.widgets import S3DirectWidget


class ProductForm(ModelForm):
    name = forms.CharField(max_length=30, label='Nome', required=True,
                                   widget=forms.TextInput(attrs={'placeholder': 'Nome'}))
    price = forms.CharField(max_length=30, label='Preço', required=True,
                                   widget=forms.TextInput(attrs={'placeholder': 'Preço'}))
    description = forms.CharField(max_length=30, label='Descrição', required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'Descrição'}))
    image = forms.URLField(label="", widget=S3DirectWidget(dest='example_destination'))
    file = forms.URLField(label="", widget=S3DirectWidget(dest='example_destination'))

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'image', 'file')