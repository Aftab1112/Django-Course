from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello, Django. This is home page")
    return render(request, "website/index.html")


def about(request):
    # return HttpResponse("About Page")
    return render(request, "website/about.html")


def contact(request):
    return HttpResponse("Contact Page")
