import datetime

from django.http import HttpResponse
from django.shortcuts import render


def display(request):
    return render(request, "myapp/first.html")


def dateTimeView(request):
    dt = datetime.datetime.now()
    s = "<b>Thew current date time is :" + str(dt)
    return HttpResponse(s)


def personalInfo(request):
    context = {"name": "Shantanu", "salary": "30000", "age": "100"}
    return render(request, "myapp/personal_info.html", context)
