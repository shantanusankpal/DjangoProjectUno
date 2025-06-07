from django.urls import path

from myapp import views

urlpatterns = [
    path("time/", views.dateTimeView),
    path("hello/", views.display),
    path("employee/", views.employees),
    path("userForm/", views.formsView),
    path("personalInfo/", views.personalInfo),
]
