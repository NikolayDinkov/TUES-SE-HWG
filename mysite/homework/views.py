from django.http.response import JsonResponse
from django.shortcuts import render
from homework.weatherApiFunc import WeatherApiFunc
from django.http import JsonResponse


def maxView(request):
    return JsonResponse(WeatherApiFunc.maxTemp(), safe=False)

def avgView(request):
    return JsonResponse(WeatherApiFunc.avgTemp(), safe=False)

def minView(request):
    return JsonResponse(WeatherApiFunc.minTemp(), safe=False)