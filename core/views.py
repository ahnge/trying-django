from django.shortcuts import render

from articles.models import Article


def home(request):
    article_list = Article.objects.all()
    context = {
        "article_list": article_list
    }
    return render(request, "home-view.html", context)