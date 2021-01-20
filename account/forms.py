from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Store
from django.db import transaction

from django.forms import ModelForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="Nome", widget=forms.TextInput(attrs={'placeholder': 'Nome'}), max_length=30,
                                 required=False)
    last_name = forms.CharField(label="Apelido", widget=forms.TextInput(attrs={'placeholder': 'Apelido'}),
                                max_length=30, required=False)
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'placeholder': 'E-mail'}), max_length=255)
   
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Repitir Senha'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name','email')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)


        user.save()

        store = Store.objects.create(user=user)
        return user
