from django.forms import ModelForm
from django import forms
from dashboard.models import Store, Order
from s3direct.widgets import S3DirectWidget
from tinymce.widgets import TinyMCE


class StoreForm(forms.ModelForm):
    name = forms.CharField(max_length=30, label='Nome da loja', required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'Nome'}))
    street_address = forms.CharField(max_length=30, label='Endereço', required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Endereço'}))
    description = forms.CharField(label="Descrição da loja ", widget=TinyMCE(attrs={}))
    logo = forms.URLField(label="Logo", widget=S3DirectWidget(dest='images'))
    instagram = forms.URLField(max_length=30, label='Instagram', required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'https://instagram.com/nodedapagina'}))
    facebook = forms.URLField(max_length=30, label='Facebook', required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'https://facebook.com/nodedapagina'}))
    twitter = forms.URLField(max_length=30, label='Twitter', required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'https://twitter.com/nodedapagina'}))
    phone_number = forms.CharField(max_length=30, label='Número de celular', required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Número de celular'}))
    city = forms.CharField(max_length=30, label='Cidade', required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Cidade'}))
    province = forms.CharField(max_length=30, label='Provincia', required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Provincia'}))
                           
    
    class Meta:
        model = Store
        fields = ( 'name', 'street_address',  'description', 'logo', "facebook",
        'twitter', 'instagram', 'city', 'province', 'phone_number',)





class StoreUpdateNameForm(forms.ModelForm):
    name = forms.CharField(max_length=30, label='Seu nome ou nome comercial - será usando como nome da sua loja', required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'Nome'}))
                         
    
    class Meta:
        model = Store
        fields = ('name',)




class StoreUpdateForm(forms.ModelForm):
    name = forms.CharField(max_length=30, label='Nome da loja', required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'Nome'}))
    street_address = forms.CharField(max_length=30, label='Endereço', required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Endereço'}))
    description = forms.CharField(label="Descrição da loja ", widget=TinyMCE(attrs={}))
    logo = forms.URLField(label="Logo", widget=S3DirectWidget(dest='images'))
    instagram = forms.URLField(max_length=30, label='Instagram', required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'https://instagram.com/nodedapagina'}))
    facebook = forms.URLField(max_length=30, label='Facebook', required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'https://facebook.com/nodedapagina'}))
    twitter = forms.URLField(max_length=30, label='Twitter', required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'https://twitter.com/nodedapagina'}))
    phone_number = forms.CharField(max_length=30, label='Número de celular', required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Número de celular'}))
    city = forms.CharField(max_length=30, label='Cidade', required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Cidade'}))
    province = forms.CharField(max_length=30, label='Provincia', required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Provincia'}))
                           
    
    class Meta:
        model = Store
        fields = ( 'name', 'street_address',  'description', 'logo', "facebook",
        'twitter', 'instagram', 'city', 'province', 'phone_number',)



