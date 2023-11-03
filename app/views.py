from .models import *
from django.http import HttpRequest
from django.shortcuts import render
from .models import *
from django.contrib.auth import *
from django.db.utils import *

def base(request):
    return render(request,'Veterinaria_list.html')
    
def guardar_perro_perro(request: HttpRequest):
    
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
