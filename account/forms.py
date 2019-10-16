from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Company
from django.db import transaction

from django.forms import ModelForm


class CompanyForm(UserCreationForm):
    commercial_name = forms.CharField(max_length=30, label='', required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Nome comercial'}))
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'placeholder': 'E-mail'}), max_length=255)
    phone_number = forms.CharField(label="Número de telefone",
                                   widget=forms.TextInput(attrs={'placeholder': 'Número de telefone'}))
    address = forms.CharField(label="Endereco",
                                   widget=forms.TextInput(attrs={'placeholder': 'Endereco'}))

    password1 = None
    password2 = None
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('commercial_name', 'address', 'phone_number', 'email')


    @transaction.atomic
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)

        default_password = "price2019" #Generate the default password

        user.set_password(default_password ) #Set de default password
        if commit:
            user.save()
            company = Company.objects.create(user=user)
            company.save()
        return user


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="Nome", widget=forms.TextInput(attrs={'placeholder': 'Nome'}), max_length=30,
                                 required=False)
    last_name = forms.CharField(label="Apelido", widget=forms.TextInput(attrs={'placeholder': 'Apelido'}),
                                max_length=30, required=False)
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'placeholder': 'E-mail'}), max_length=255)
    phone_number = forms.CharField(label="Número de telefone",
                                   widget=forms.TextInput(attrs={'placeholder': 'Número de telefone'}))

    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Repitir Senha'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone_number', 'email')
