from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def contact(request):
    return HttpResponse("This is Contact Us Page")


def about(request):
    return HttpResponse("This is About Us Page")
