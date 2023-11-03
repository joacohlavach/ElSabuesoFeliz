from django.shortcuts import render
from .models import *
from django.http import HttpRequest

def base(request: HttpRequest):
    
    return render(request,'Veterinaria_list.html')
    
def guardar_perro(request: HttpRequest):

    if request.method == 'POST':
        nombreperro = request.POST['Nombre']
        nombreperro = request.POST['Nombre']
        Perro.objects.create(nombreperro)
    else:
        return render(request,"LoginPerros.html")
   

def razaperro(request):
    return render(request, 'razaperro_template.html')

def hola (request):
    ...

