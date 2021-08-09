from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    description = models.CharField(max_length=50, verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado en")
    
    class Meta:
        verbose_name = "Categoriá"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name

class Article(models.Model):

    title = models.CharField(max_length=50, verbose_name="Título")
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(upload_to="articles", default='null', verbose_name="Imagen")
    public = models.BooleanField(verbose_name="Público")
    user = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorías", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado en")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Creado en")

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulo"

    def __str__(self):
        return self.title



