from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import User

# Create your views here.
def index(request):
    return render(request, 'home/home.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Formdan verileri al
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # Kullanıcıyı veritabanında ara
            user = User.objects.filter(username=username, password=password).first()
            
            # Kullanıcı varsa ana sayfaya yönlendir
            if user:
                return redirect('dashboard')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    
    return render(request, 'home/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Formdan verileri al
            username = form.cleaned_data.get('username')
            name = form.cleaned_data.get('name')
            surname = form.cleaned_data.get('surname')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            password_repeat = form.cleaned_data.get('password_repeat')
            
            # Şifrelerin eşleşip eşleşmediğini kontrol et
            if password == password_repeat:
                new_user = User(
                    username=username,
                    name=name,
                    surname=surname,
                    email=email,
                    password=password
                )
                new_user.save()
                
                # Kayıt işleminden sonra login sayfasına yönlendir
                return redirect('login')
            else:
                form.add_error('password_repeat', 'Passwords do not match')
    else:
        form = RegisterForm()
        
    return render(request, 'home/register.html', {'form': form})

def forgotPassword(request):
    return render(request, 'home/forgot-password.html')

def resetPassword(request):
    return render(request, 'home/reset-password.html')
