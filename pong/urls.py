from django.urls import path
from . import views

urlpatterns = [
    path('', views.pong_func, name='pong'),
    path('pongmulti/', views.pongmulti_func, name='pongmulti'),

]