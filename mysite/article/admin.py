from django.contrib import admin
from article.models import Article
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "created_time", "last_updated_time", "is_deleted", 'read_num')
    # 按照id正序
    ordering = ("id",)
    # 按照id倒序
    # ordering = ("-id",)

# 可以改写为 @admin.register(Article)
# admin.site.register(Article, ArticleAdmin)