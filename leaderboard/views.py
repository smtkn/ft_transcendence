from django.shortcuts import render

# Create your views here.

def leaderboard(request):
    return render(request, 'leaderboard/index.html')