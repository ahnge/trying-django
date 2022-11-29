from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Article
from .forms import ArticleForm

# Create your views here.


def article_detail_view(request, slug=None):
    article = None
    if slug is not None:
        article = get_object_or_404(Article, slug=slug)

    context = {"object": article}
    return render(request, "articles/article_detail.html", context)


@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        article_obj = form.save()
        context["object"] = article_obj
        return redirect("articles:article_detail", slug=article_obj.slug)
    return render(request, "articles/article_create.html", context)


def article_search_view(request):
    query_dict = request.GET
    q = query_dict["q"]

    if q is not None:
        try:
            article_list = Article.objects.search(query=q)
        except:
            article_list = None

    context = {"object_list": article_list}
    return render(request, "articles/search.html", context)
