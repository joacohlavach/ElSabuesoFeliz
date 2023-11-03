from django.contrib import admin
from .views import *
from django.urls import path
from . import views
urlpatterns = [
    path('', views.base, name = 'main'),
    path("login/",views.guardar_perro, name= 'login'),
    path('razas/', views.razaperro, name='Raza'),


]