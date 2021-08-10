from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'index.html', {'title': 'inicio'})

def register_page(request):

    if request.user.is_authenticated:
        return redirect("home")

    register_form = RegisterForm()

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Registrado exitosamente')
            return redirect('home')

    return render(request, 'users/register.html', {
        'title': 'Registro',
        'register_form': register_form
    })

def login_page(request):

    if request.user.is_authenticated:
        return redirect("home")
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Usuario no autenticado')

    return render(request, 'users/login.html', {
        'title': 'Login '
    })

def logout_user(request):
    logout(request)
    return redirect('Login')