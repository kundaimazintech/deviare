from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests

# Create your views here.


@login_required()
def get_weather(request):
    api_key = "3de49393e4baaf1d1a4a326034002890"
    city_id = "993800"
    url = "http://api.openweathermap.org/data/2.5/forecast"
    querystring = {"id": 993800, "appid": api_key }
    responses = requests.request("GET", url, params=querystring)
    from django.http import JsonResponse, response, HttpResponse
    # return JsonResponse(responses.content, safe=False)

    return HttpResponse(responses.content)


def save_weather(request):
    return request


def view_weather():
    return


