from django.contrib import admin

from article.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'created_at', 'updated_at', 'is_published', 'view_count',)
    list_filter = ('is_published',)
    search_fields = ('title',)
