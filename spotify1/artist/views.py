from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def view1(request):
     
    # template = loader.get_template ( 'artist/1.html')
    # return HttpResponse(template.render())
    context={
        "name":["SPB","S.janaki"],
        "bio":["popular singer in kannada","popular female singer in kannada"],
        "default":None,
        "song":["Hosa belaku","Anuraga"],
        "released_date":[datetime(2026,1,26,10),datetime(2026,1,26)],
                }
    return render(request,'artist/artist.html',context)

def home(request):
    return render(request, 'base.html')

    




# Create your views here.
