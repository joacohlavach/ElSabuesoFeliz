from django.shortcuts import render
from .models import Veterinaria

# Create your views here.
def Veterinaria_list(request):
    veterinaria = Veterinaria.objects.all()
    return render(request, 'app/Veterinaria_list.html', {'veterinaria': veterinaria})