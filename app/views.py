from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import *
from django.contrib.auth import *
from django.db.utils import *

def base(request):
    return render(request,'Veterinaria_list.html')
    
def login_perro(request):
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


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            return render(request, "Veterinaria_list.html", {'error_message': 'Credenciales inválidas'})
        else:
            return render(request, self.template_name, {'error_message': 'Credenciales inválidas'})
