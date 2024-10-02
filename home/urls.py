from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('forgot-pasaword/', views.forgotPassword, name='forgot-password'),
    path('reset-password/', views.resetPassword, name='reset-password'),
]
