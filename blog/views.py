from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
import random
from blog.models import Article
from django.http import Http404


# Create your views here.
def index(request):
    if request.method == "POST":
        article = Article(title=request.POST["title"], body=request.POST["text"])
        article.save()
        return redirect(detail, article.id)
    context = {"articles": Article.objects.all()}

    return render(request, "blog/index.html", context)


def hello(request):

    fortune = random.randint(1, 3)
    isGreatFortune = False
    fortuneMesseage = ""

    if fortune == 1:
        isGreatFortune = True
        fortuneMesseage = "Great Fortune!"
    elif fortune == 2:
        fortuneMesseage = "Small Fortune"
    elif fortune == 3:
        fortuneMesseage = "Bad Fortune..."

    data = {
        "name": "Alice",
        "weather": "CLOUDY",
        "weather_detail": ["Temperature: 23℃", "Humidity: 48%", "Wind: 5m/s"],
        "isGreatFortune": isGreatFortune,
        "fortune": fortuneMesseage,
    }
    return render(request, "blog/hello.html", data)


def redirect_test(request):
    return redirect(hello)


def detail(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    context = {"article": article}
    return render(request, "blog/detail.html", context)


def update(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    context = {"article": article}
    return render(request, "blog/edit.html", context)


def delete(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    article.delete()
    return redirect(index)
