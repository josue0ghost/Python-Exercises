"""LearningDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings

# Import myapp
from myapp import views

urlpatterns = [
    path('', views.index, name="home"),
    path('admin/', admin.site.urls),
    path('hello-world/', views.hello_world, name="hello_world"),
    path('test-page/', views.page, name="test"),
    path('test-page/<int:id>', views.page, name="test"),
    path('contact/', views.contact, name="contact"),
    path('contact/<str:name>', views.contact, name="contact"),

    path('article/', views.article, name="get_article"),

    path('article/create', views.save_article_view, name="save_article_view"),
    path('article/save', views.save_article, name="save_article"),
    path('article/save_full_article', views.save_full_article_view, name="save_full_article"),
    path('article/create/<str:title>/<str:content>/<str:public>/', views.create_article, name="create_user"),

    path('article/edit/<int:id>', views.edit_article),
    path('article/delete/<int:id>', views.delete_article, name="delete_article"),
    path('articles/', views.articles, name="articles"),
]

# conf to upload images
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)