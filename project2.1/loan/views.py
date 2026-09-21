from django.shortcuts import render
from .forms import form1

def view1(request):
    if request.method=="POST":
        form=form1(request.POST)
        if form.is_valid():
            return render(request,'loan/1.html',{'form':form})
    else:

        form=form1()
        return render(request,'loan/1.html',{'form':form})

# Create your views here.
