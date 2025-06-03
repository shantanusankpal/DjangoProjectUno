from django.urls import path

from myapp import views

urlpatterns = [
    path("time/", views.dateTimeView),
    path("hello/", views.display),
    path("personalInfo/", views.personalInfo),
]
