from django.urls import path
from . import views

urlpatterns = [
    path("todos-los-articulos/", views.list_articles, name="Article list"),
    path("categoria/<int:category_id>", views.category, name="Category"),
    path("articulo/<int:article_id>", views.article, name="Article")
]
