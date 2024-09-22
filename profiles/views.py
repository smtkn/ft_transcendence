from django.shortcuts import render

# Create your views here.

def profiles(request):
    return render(request, 'base.html', {'current_page': 'profiles/index.html'})

def profileRaw(request):
    return render(request, 'profiles/index.html')