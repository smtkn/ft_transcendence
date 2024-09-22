from django.urls import path
from . import views

urlpatterns = [
    path('', views.game, name='game'),
    path('raw/', views.gameRaw, name='gameRaw'),
]
