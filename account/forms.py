from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Company
from django.db import transaction

from django.forms import ModelForm


class CompanyForm(UserCreationForm):
    phone_number = forms.CharField(max_length=30, label='', required=True,
                                   widget=forms.TextInput(attrs={'placeholder': 'Numero de telefone'}))
    commercial_name = forms.CharField(max_length=30, label='', required=True,
                                   widget=forms.TextInput(attrs={'placeholder': 'Nome da empresa'}))

    email = forms.EmailField(max_length=254, label='',  widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
    address = forms.CharField(max_length=30, label='', required=True,
                                      widget=forms.TextInput(attrs={'placeholder': 'Endereco'}))

    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Repitir Senha'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('commercial_name', 'phone_number',  'email', 'address', 'password1', 'password2')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_active = False
        user.is_business = True

        user.save()

        company = Company.objects.create(user=user)
        return user


