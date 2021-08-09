from django.contrib import admin
from .models import Category, Article

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', 'user')

    def save_model(self, request, obj, form, change):
      obj.user_id = request.user.id
      obj.save()

