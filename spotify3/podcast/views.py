from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import form1

def view1(request):
    if request.method=="POST":
        form=form1(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            print(form.errors)
    else:

        form=form1()

    # template = loader.get_template('podcast/podcast.html')
    # return HttpResponse(template.render())
    return render(request,"podcast/podcast.html",{"form":form})
# Create your views here.
