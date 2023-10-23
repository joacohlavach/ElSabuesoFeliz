from django.contrib import admin
from .views import *
from django.urls import include
from django.urls import path

urlpatterns = [
    path('', base, name = 'main'),
    path('login/', login, name = 'loginPerro'),
    path('razas/', razaperro, name='Raza'),

    path('inicio/', views.inicio_view, name='inicio'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
]
    
