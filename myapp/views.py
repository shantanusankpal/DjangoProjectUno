import datetime

from django.http import HttpResponse
from django.shortcuts import render

from myapp.models import Employee


def display(request):
    return render(request, "myapp/first.html")


def employees(request):
    employee1 = Employee.objects.all()
    actual_employee = employee1[0]
    return render(request, "myapp/person.html", {"employee": actual_employee})


def dateTimeView(request):
    dt = datetime.datetime.now()
    s = "<b>Thew current date time is :" + str(dt)
    return HttpResponse(s)


def personalInfo(request):
    context = {"name": "Shantanu", "salary": "30000", "age": "100"}
    return render(request, "myapp/personal_info.html", context)
