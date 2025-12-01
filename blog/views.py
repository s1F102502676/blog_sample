from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone


# Create your views here.
def index(request):
    context = {"articles": []}

    return render(request, "blog/index.html", context)


def hello(request):
    import random

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
    context = {"article_id": article_id}
    return render(request, "blog/tbd.html", context)


def update(request, article_id):
    context = {"artcle_id": article_id}
    return render(request, "blog/tbd,html", context)


def delete(request, article_id):
    return redirect(index)
