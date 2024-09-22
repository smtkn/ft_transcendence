from django.shortcuts import render

# Create your views here.

def leaderboard(request):
    return render(request, 'base.html', {'current_page': 'leaderboard/index.html'})

def leaderboardRaw(request):
    return render(request, 'leaderboard/index.html')