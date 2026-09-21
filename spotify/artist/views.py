from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

def view1(request):
    name="SPB"
     
    template = loader.get_template ( 'artist/artist.html')
    return HttpResponse(template.render({"name1":name}))
   

def home(request):
    return render(request, "base.html")

    




# Create your views here.
