from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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
            commercial_name = form.cleaned_data.get('commercial_name')
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone_number')
            address = form.cleaned_data.get('address')
            form.save()

            account_sid = 'AC7314ed7fc30559b0e1c8454743de686a'
            auth_token = 'c23acf7ad601d3957598561fe575eee8'
            client = Client(account_sid, auth_token)
            number_id = "Preco"
            send_mail(
                f'''Preço''',
                f'''E-mail de registo
                    Mais uma vez obrigado pelo registo.
                    Esperamos lhe trazer mais vendas com esta parceria.
                    Os seus dados de acesso ao preco.co.mz são
                    Utilizador –{commercial_name}@preco.co.mz
                    Senha – preco2019 
                    
             
                 

                ''',
                'conta@preco.co.mz',
                [email],
                fail_silently=False,
            )
            message = client.messages.create(
                body=f'''A empresa
                          {commercial_name} foi regista no preço com os seguintes detalhes
                         Name :{commercial_name}
                        Email : {commercial_name}@preco.co.z
                        Numero de telefone {phone_number}
                        Address {address}
                ''',
                from_=number_id,
                to=phone_number
            )
            user = authenticate(username=email, password="price2019")
            if user is not None:
                login(request, user)
                return redirect('confirm')


    else:
        form = CompanyForm()
    return render(request, 'account/company.html', {'form': form})


def confirm(request):
    return render(request, 'account/confirm.html')


@login_required(login_url='/account/signin/')
def logout_view(request):
    logout(request)
    return redirect('signin')
    # Redirect to a succe
