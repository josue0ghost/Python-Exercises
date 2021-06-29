from django.contrib import admin
from .models import *

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Article)
admin.site.register(Category)


# conf. admin title
admin.site.site_header = "Panel de adminsitración :)"
admin.site.site_title = "Panel de admin"
admin.site.index_title = "Panel"