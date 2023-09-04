from django.http import HttpResponse
from django.shortcuts import render

# def home(request):
#     return render(request, 'home.html')


def home(request):
    return HttpResponse("<h1>Blog Home</h1>")


def about(request):
    return HttpResponse("<h1>Blog About Page</h1>")
