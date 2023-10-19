from django.contrib import admin
from .views import base
from django.urls import path

urlpatterns = [
    path('', base, name = 'main'),
    path('login/', base, name = 'login')
]