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


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="Nome", widget=forms.TextInput(attrs={'placeholder': 'Nome'}), max_length=30, required=False)
    last_name = forms.CharField(label="Apelido", widget=forms.TextInput(attrs={'placeholder': 'Apelido'}), max_length=30, required=False)
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'placeholder': 'E-mail'}), max_length=255)
    phone_number = forms.CharField(label="Número de telefone", widget=forms.TextInput(attrs={'placeholder': 'Número de telefone'}))

    password1 = forms.CharField(label='',  widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))
    password2 = forms.CharField(label='',  widget=forms.PasswordInput(attrs={'placeholder': 'Repitir Senha'}))

    class Meta:
            model = User
            fields = ('first_name',  'last_name', 'phone_number', 'email')

