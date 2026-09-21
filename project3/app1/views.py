from django.shortcuts import render
from .forms import form1
from .models import model1

def view1(request):
    if request.method=="POST":
        form=form1(request.POST)
        if form.is_valid():
            form.save()
            name=form.cleaned_data['name']
            p=form.cleaned_data['principle']
            r=form.cleaned_data['rate']
            t=form.cleaned_data['time']

            context={
                "name":name,
                "p":p,
                "r":r,
                "t":t,
            }
            return render(request,"app1/1.html",context)
    else:        
        form=form1()
    return render(request,"app1/1.html",{"form":form})

def view2(request):
    record=model1.objects.all()
    return render(request,"app1/2.html",{"record":record})


