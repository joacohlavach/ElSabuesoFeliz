from django.contrib import admin
from .views import *
from django.urls import path

urlpatterns = [
    path('', base, name = 'main'),
    path('login/', login, name = 'loginPerro'),
    path('razas/', razaperro, name='Raza'),
]
