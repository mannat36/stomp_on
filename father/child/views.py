from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.

def child(request):
    template = loader.get_template("about.html")
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())

def services(request):
    template = loader.get_template("services.html")
    return HttpResponse(template.render())

def gallery(request):
    template = loader.get_template("gallery.html")
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template("contact.html")
    return HttpResponse(template.render())

