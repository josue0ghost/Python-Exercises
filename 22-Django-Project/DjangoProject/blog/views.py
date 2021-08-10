from django.shortcuts import render, get_object_or_404
from blog.models import Category, Article
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="Login")
def list_articles(request):

  articles = Article.objects.all()
  
  paginator = Paginator(articles, 2)

  page= request.GET.get('page')
  page_articles = paginator.get_page(page)

  return render(request, 'articlelist.html', {
    'title': 'Artículos',
    'articles': page_articles
  })

@login_required(login_url="Login")
def category(request, category_id):
  category = get_object_or_404(Category, id=category_id)
  articles = Article.objects.filter(categories=category_id)

  paginator = Paginator(articles, 2)

  page= request.GET.get('page')
  page_articles = paginator.get_page(page)

  return render(request, 'category.html', {
    'category': category,
    'articles': page_articles
  })

@login_required(login_url="Login")
def article(request, article_id):
  article = get_object_or_404(Article, id=article_id)

  return render(request, 'article_detail.html', {
    'article': article
  })