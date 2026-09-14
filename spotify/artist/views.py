from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

def view1(request):
    template = loader.get_template ( 'artist/1.html')
    return HttpResponse(template.render())

def home(request):
    return render(request, 'home1.html')



# Create your views here.
