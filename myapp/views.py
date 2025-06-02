import datetime

from django.http import HttpResponse
from django.shortcuts import render


def display(request):
    return HttpResponse("<h1>First view</h1>")


def dateTimeView(request):
    dt = datetime.datetime.now()
    s = "<b>Thew current date time is :" + str(dt)
    return HttpResponse(s)
