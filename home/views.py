from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'home/login.html')

def register(request):
    return render(request, 'home/register.html')

def forgotPassword(request):
    return render(request, 'home/forgot-password.html')

def resetPassword(request):
    return render(request, 'home/reset-password.html')
