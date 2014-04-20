from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says: Hello world! <p> <a href='/rango/about'>About</a> </p>")

def about(request):
    return HttpResponse("This is the about page <a href='/rango'>Back to homepage</a>")
