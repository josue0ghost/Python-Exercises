from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home/', views.index, name="home"),
    path('register/', views.register_page, name="Register"),
    path('login/', views.login_page, name="Login"),
    path('logout/', views.logout_user, name="Logout")
]
