from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.urls import reverse_lazy
from twilio.rest import Client
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import CompanyForm, SignUpForm
from django.core.mail import send_mail


def signin(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "E-mail e senha não correspodem.")
    return render(request, 'account/signin.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('index')

    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})


def company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            commercial_name = form.cleaned_data.get('commercial_name')
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone_number')
            address = form.cleaned_data.get('address')

            account_sid = 'AC7314ed7fc30559b0e1c8454743de686a'
            auth_token = 'c23acf7ad601d3957598561fe575eee8'
            client = Client(account_sid, auth_token)
            number_id = "Preco"
            send_mail(
                f''' Os Detalhes da sua conta',
                   Encontre aqui os dados para activacao da tua conta'
                   Nome: {commercial_name}
                   Email: {email}
                    
                ''',
                'conta@preco.co.mz',
                [email],
                fail_silently=False,
            )
            message = client.messages.create(
                body=f'''A empresa {commercial_name} foi registada no preço com os seguintes detalhes
                        Name :{commercial_name}
                        Email : {email}
                        Numero de telefone {phone_number}
                        Address {address}
                ''',
                from_=number_id,
                to="+258849394995"
            )
            return redirect('confirm')


    else:
        form = CompanyForm()
    return render(request, 'account/company.html', {'form': form})


def confirm(request):
    return render(request, 'account/confirm.html')


@login_required()
def logout_view(request):
    logout(request)
    # Redirect to a succe
