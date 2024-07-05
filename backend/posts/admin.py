from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Admin View for Article)"""

    list_display = (
        "title",
        "content",
        "created_at",
        "updated_at",
    )
