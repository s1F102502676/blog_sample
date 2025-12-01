from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "blog/index.html")


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
