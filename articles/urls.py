from django.urls import path
from .views import article_detail_view, article_search_view, article_create_view

app_name = "articles"

urlpatterns = [
    path("create/", article_create_view, name="article_create"),
    path("<int:id>/", article_detail_view, name="article_detail"),
    path("search/", article_search_view, name="search_article"),
]
