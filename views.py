from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def base(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())

def django(request):
    template = loader.get_template('django.html')
    return HttpResponse(template.render())

def menu(request):
    template = loader.get_template('menu.html')
    return HttpResponse(template.render())

def menu1(request):
    template = loader.get_template('menu1.html')
    return HttpResponse(template.render())  
