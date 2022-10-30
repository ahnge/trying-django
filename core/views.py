import random
from django.http import HttpResponse


def home(request):
    number = random.randint(1, 10000)
    HTML_STRING = f"""
    <h1>Hello world {number}</h1>
    """
    return HttpResponse(HTML_STRING)