from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('d/', views.d, name='d'),
    
]
