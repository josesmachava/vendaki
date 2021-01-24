from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from .forms import  SignUpForm
from .models import Store

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
                store = Store.objects.get(user=user)
                return redirect('update-store-name', store.id)

    else:
        form = SignUpForm()
    return render(request, 'account/signup.jade', {'form': form})



def profile(request):
    return render(request, 'account/profile.pug')


def confirm(request):
    return render(request, 'account/confirm.html')


@login_required(login_url='/account/signin/')
def logout_view(request):
    logout(request)
    return redirect('signin')
    # Redirect to a succe
