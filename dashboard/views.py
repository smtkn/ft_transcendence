from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'base.html', {'current_page': 'dashboard/index.html'})

def dashboardRaw(request):
    return render(request, 'dashboard/index.html')