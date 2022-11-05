from django.urls import path
from .views import article_detail_view, article_search_view

app_name = "articles"

urlpatterns = [
    path('<int:id>/', article_detail_view, name="article_detail"),
    path('search/', article_search_view, name="search_article"),
]
