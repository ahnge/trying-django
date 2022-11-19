from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "created_at", "updated_at", "slug"]
    search_fields = ["title", "content"]


admin.site.register(Article, ArticleAdmin)
