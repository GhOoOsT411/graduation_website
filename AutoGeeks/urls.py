from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('Registration/', views.Registration, name='Registration'),
    path('Login/', views.Login, name='Login'),
]