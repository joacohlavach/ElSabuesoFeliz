from django.shortcuts import render
from .models import *

def base(request):
    return render(request,'Veterinaria_list.html')
    
def login(request):
    if request.method == 'GET':
        return render(request, 'LoginPerros.html')
    
    else:
        perro = request.POST["Nombre"]
        raza =request.POST["Raza"]
        peso = request.POST["Peso"]
        sexo = request.POST["genero"]
        p = Perro.objects.create(nombre=perro,raza=raza,peso=peso,sexo=sexo)
        print (p)
def razaperro(request):
    return render(request, 'razaperro_template.html')

def hola (request):
    ...

