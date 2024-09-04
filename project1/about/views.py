from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def about(request):
    template = loader.get_template('about.html')
    template = loader.get_template('static.html')
    return HttpResponse(template.render())

