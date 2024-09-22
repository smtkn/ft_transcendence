from django.shortcuts import render

# Create your views here.
def chat(request):
    return render(request, 'base.html', {'current_page': 'chat/index.html'})

def chatRaw(request):
    return render(request, 'chat/index.html')