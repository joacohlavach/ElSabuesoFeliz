from django.contrib import admin
from .views import *
from django.urls import path 
from django.urls import path, include

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('veterinaria/', base, name = 'Veterinarialist'),
    path('razas/', razaperro, name='Raza')

]