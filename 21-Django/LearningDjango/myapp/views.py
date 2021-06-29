from django.http import response
from django.shortcuts import render, HttpResponse, redirect
from myapp.models import Article
from myapp.forms import FormArticle
from django.contrib import messages

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

def edit_article(request, id):
    article = Article.objects.get(pk=id)

    article.title = "Batman"
    article.content = "2017 movie"
    article.public = True
    article.save()

    response = f"articulo editado: {article.title}"
    return HttpResponse(response)

def articles(request):
    articles = Article.objects.all()
    # articles = Article.objects.order_by('title')
    # articles = Article.objects.order_by('-title')
    # articles = Article.objects.all()[:5]   #---> LIMIT 5
    # articles = Article.objects.all()[3:5]  #---> BETWEEN 3 TO 5
    # articles = Article.objects.filter(title__contains="batman") # __contains, __exact, __iexact
    # articles = Article.objects.filter(id__gt=3) # __gte, __lt, __lte (>, >=, <, <=)
    # articles = Article.objects.filter(title="super").exclude(public=True)
    # articles = Article.objects.filter(Q(title__contains="ss") | Q(title__contains="gg"))
    # articles = Article.objects.raw("SLECT * FROM TABLE")
    return render(request, 'articles.html', {
        'articles': articles
    })

def delete_article(request, id):
    article = Article.objects.get(pk=id)
    article.delete()

    return redirect('articles')


def save_article(request):
    if request.method == 'POST':

        article = Article(
            title = request.POST['title'],
            content = request.POST['content'],
            public = request.POST['public']
        )

        # guarda info en la bdd
        article.save()
        return HttpResponse("")
    else:
        return HttpResponse("Err")

def save_article_view(request):
    return render(request, 'create_article.html')

def save_full_article(request):

    if request.method == 'POST':
        form = FormArticle(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            article = Article(
                title = data.get('title'),
                content = data.get('content'),
                public = data.get('public'),
            )

            # guarda info en la bdd
            article.save()

            # mensaje flash
            messages.success(request, 'Article created')

            return HttpResponse("")
        else:
            return HttpResponse("Err")
    else:
        return HttpResponse("Err")

def save_full_article_view(request):
    form = FormArticle()
    return render(request, 'save_full_article.html', {'form': form})
