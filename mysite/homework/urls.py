from django.contrib import admin
from django.urls import path
from homework.views import maxView, avgView, minView

urlpatterns = [
    path('max', maxView),
    path('avg', avgView),
    path('min', minView),
]
