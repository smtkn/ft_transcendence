from django.shortcuts import render

# Create your views here.

def game(request):
    return render(request, 'base.html', {'current_page': 'game/index.html'})

def gameRaw(request):
    return render(request, 'game/index.html')