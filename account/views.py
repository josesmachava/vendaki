from django.shortcuts import render

# Create your views here.



def signin(request):



    return render(request, 'account/signin.html')








def signup_company(request):



    return render(request, 'account/signup_company.html')







def signup_user(request):



    return render(request, 'account/signup_user.html')