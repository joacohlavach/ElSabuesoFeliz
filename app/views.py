from django.shortcuts import render
from .models import *

def base(request):
    return render(request,'Veterinaria_list.html')
    
def login(request):
    return render(request, 'LoginPerros.html')

def razaperro(request):
    return render(request, 'razaperro_template.html')