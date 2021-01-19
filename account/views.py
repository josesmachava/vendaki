from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from twilio.rest import Client
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from .forms import  SignUpForm
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



def profile(request):
    return render(request, 'account/profile.jade')


def confirm(request):
    return render(request, 'account/confirm.html')


@login_required(login_url='/account/signin/')
def logout_view(request):
    logout(request)
    return redirect('signin')
    # Redirect to a succe
