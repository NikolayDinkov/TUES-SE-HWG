

from django.http import request
import requests

class WeatherApiFunc():
    def __init__(self):
        pass

    def maxTemp(self):
        weather = requests.post("https://tues2022.proxy.beeceptor.com/my/api/test").json()["data"]
        maxTmp = weather[0]["temperature"]
        for day in weather:
            if(day["temperature"] > maxTmp):
                maxTmp = day["temperature"]
        return maxTmp


    def avgTemp(self):
        weather = requests.post("https://tues2022.proxy.beeceptor.com/my/api/test").json()["data"]
        return sum([day["temperature"] for day in weather])/len(weather)

    def minTemp(self):
        weather = requests.post("https://tues2022.proxy.beeceptor.com/my/api/test").json()["data"]
        minTmp = weather[0]["temperature"]
        for day in weather:
            if(day["temperature"] < minTmp):
                minTmp = day["temperature"]
        return minTmp