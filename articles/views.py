from django.shortcuts import render

from .models import Article

# Create your views here.

def article_detail_view(request, id=None):
    article = None
    if id is not None:
        try:
            article = Article.objects.get(pk=id)
        except:
            article = None
    context = {"object": article}
    return render(request, "articles/article_detail.html", context)


def article_search_view(request):
    query_dict = request.GET
    q = query_dict["q"]

    try:
        article_id = int(q)
    except:
        article_id =None

    if article_id is not None:
        try:
            article_obj = Article.objects.get(id=article_id)
        except:
            article_obj = None
    
    context = {'object': article_obj}
    return render(request, 
    "articles/search.html", context)

