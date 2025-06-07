import datetime

from django.http import HttpResponse
from django.shortcuts import render

from myapp.models import Employee
from myapp.forms import UserRegistrationForm


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


def formsView(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            print(f"First Name is {form.cleaned_data['firstName']}")
            print(f"last Name is {form.cleaned_data['lastName']}")
        else:
            form = UserRegistrationForm()
    return render(request, "myapp/formsForUser.html", {"form": form})


def personalInfo(request):
    context = {"name": "Shantanu", "salary": "30000", "age": "100"}
    return render(request, "myapp/personal_info.html", context)
