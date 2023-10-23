from django.shortcuts import render
from .models import *

def base(request):
    return render(request,'Veterinaria_list.html')
    
def login(request):
    if request.method == 'GET':
        return render(request, 'LoginPerros.html')
    
    else:
        p = Perro.objects.create()

def razaperro(request):
    return render(request, 'razaperro_template.html')

def hola (request):
    ...

