from django.shortcuts import render
from .models import *
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required

def base(request):
    return render(request,'Veterinaria_list.html')
    
def login(request):
    return render(request, 'LoginPerros.html')

def razaperro(request):
    return render(request, 'razaperro_template.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
