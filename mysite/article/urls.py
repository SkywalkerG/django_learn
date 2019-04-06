from django.urls import path, re_path
from article.views import article_detail, article_list

urlpatterns = [
    path('<int:article_id>', article_detail, name='article_detail'),
    path('', article_list, name='article_list')
]