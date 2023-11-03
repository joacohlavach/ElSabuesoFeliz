from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.base, name = 'main'),
    path("login/",views.guardar_perro, name= 'login'),
    path('razas/', views.razaperro, name='Raza'),


]