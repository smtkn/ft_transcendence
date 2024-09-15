from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def pong_func(request):
    return render(request, 'pong/pong.html')

def pongmulti_func(request):
    return render(request, 'pong/pongmulti.html')