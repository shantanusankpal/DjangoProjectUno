from django.shortcuts import render
from django.http import HttpResponse


def quote(request):
    return HttpResponse("This is a sample quote.")


# Create your views here.
