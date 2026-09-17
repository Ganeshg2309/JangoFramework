from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def view1(request):
    template = loader.get_template('podcast/1.html')
    return HttpResponse(template.render())


# Create your views here.
