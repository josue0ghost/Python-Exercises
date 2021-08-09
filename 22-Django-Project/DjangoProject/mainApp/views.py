from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {'title': 'inicio'})

def register_page(request):
    return render(request, 'users/register.html', {
        'title': 'Registro'
    })