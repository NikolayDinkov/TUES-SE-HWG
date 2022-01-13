

from django.http import request
import requests

class WeatherApiFunc():
    def __init__(self):
        pass

    @staticmethod
    def maxTemp():
        weather = requests.post("https://tues2022.proxy.beeceptor.com/my/api/test").json()["data"]
        maxTmp = weather[0]["temperature"]
        for day in weather:
            if(day["temperature"] > maxTmp):
                maxTmp = day["temperature"]
        return maxTmp

    @staticmethod
    def avgTemp():
        weather = requests.post("https://tues2022.proxy.beeceptor.com/my/api/test").json()["data"]
        return sum([day["temperature"] for day in weather])/len(weather)

    @staticmethod
    def minTemp():
        weather = requests.post("https://tues2022.proxy.beeceptor.com/my/api/test").json()["data"]
        minTmp = weather[0]["temperature"]
        for day in weather:
            if(day["temperature"] < minTmp):
                minTmp = day["temperature"]
        return minTmp