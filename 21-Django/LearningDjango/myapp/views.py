from django.http import response
from django.shortcuts import render, HttpResponse, redirect
from myapp.models import Article

# Create your views here.

layout = """
    <h1>Django web page</h1>
    <hr/>
    <ul>
        <li>
            <a href="/">Home</a>
        </li>
        <li>
            <a href="/hello-world">Hello World</a>
        </li>
        <li>
            <a href="/test-page">Test page</a>
        </li>
        <li>
            <a href="/contact">Contact</a>
        </li>
    </ul>
    <hr/>
"""


def index(request):
    year = 2021
    list_of_years = range(year, 2050)

    return render(request, 'index.html', {
        'my_var': 'context data',
        'years': list_of_years
    })

def hello_world(request):
    return render(request, 'hola_mundo.html')

def page(request, id=0):
    if id == 1:
        return redirect('/')

    return render(request, 'pagina.html', {
        'text': '',
        'list': [1, 2, 3]
    })

def contact(request, name=""):
    return HttpResponse(layout+f"""
        <h1>Contact<h1>
        <h2>{name}<h2>
    """)

def create_article(request, title, content, public):
    article = Article(
        title = title,
        content = content,
        public = public
    )

    # guarda info en la bdd
    article.save()

    return HttpResponse("")

def article(request):

    try:
        article = Article.objects.get(pk=1, title="something", public=True)
        response = f"articulo: {article.title}"
    except:
        response = "articulo no encontrado"
    return HttpResponse(response)