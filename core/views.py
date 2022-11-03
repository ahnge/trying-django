import random
from django.http import HttpResponse
from django.template.loader import render_to_string

from articles.models import Articles


def home(request):
    number = random.randint(1, 2)
    article_obj = Articles.objects.get(pk=number)
    article_list = Articles.objects.all()
    context = {
        "article_list": article_list
    }
    HTML_STRING = render_to_string("home-view.html", context=context)
    return HttpResponse(HTML_STRING)