from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.db import transaction
from django.forms import ModelForm

class CompanyForm(UserCreationForm):
    commercial_name = forms.CharField(max_length=30, label='',  required=True, widget=forms.TextInput(attrs={'placeholder': 'Nome da empresa'}))
    phone_number = forms.CharField(max_length=30, label='', required=True  , widget=forms.TextInput(attrs={'placeholder': 'Numero de telefone'}))
    email = forms.EmailField(max_length=254, label='',  widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
    address = forms.CharField(max_length=30, label='', required=True  , widget=forms.TextInput(attrs={'placeholder': 'Endereço'}))
    password1 = forms.CharField(label='',  widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))
    password2 = forms.CharField(label='',  widget=forms.PasswordInput(attrs={'placeholder': 'Repitir Senha'}))
    
    
   

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('commercial_name', 'phone_number', 'email', 'address')
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_company = False
        
        user.save()
        user.set_password('price2019')
        company = Company.objects.create(user=user)
        return user        


class ProfileForm(UserCreationForm):
    name = forms.CharField(max_length=30, label='',  required=True, widget=forms.TextInput(attrs={'placeholder': 'Nome'}))
    phone_number = forms.CharField(max_length=30, label='', required=True  , widget=forms.TextInput(attrs={'placeholder': 'Numero de telefone'}))
    email = forms.EmailField(max_length=254, label='',  widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
    password1 = forms.CharField(label='',  widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))
    password2 = forms.CharField(label='',  widget=forms.PasswordInput(attrs={'placeholder': 'Repitir Senha'}))
    
    
   

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('name', 'phone_number', 'email')
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_company = False
        
        user.save()
        user.set_password('price2019')
        profile = Profile.objects.create(user=user)
        return user        
