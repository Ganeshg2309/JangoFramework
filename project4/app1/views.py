from django.shortcuts import render
from .forms import form1
from .models import model1

def view1(request):
    if request.method=="POST":
        form=form1(request.POST)
        form.save()  
        if form.is_valid():
            form.save()  
            name=form.cleaned_data['name']
            p=form.cleaned_data['p']
            t=form.cleaned_data['t']
            r=form.cleaned_data['r']
            n=t*12
            monthly_rate=(r/(12*100))
            monthly_emi=((p*monthly_rate)*((1+monthly_rate)**n))/(((1+monthly_rate)**n)-1)
            total_ammount=monthly_emi*n
            interest=p-total_ammount


            context = {
                "name":name,
                "p":p,
                "t":t,
                "r":r,
                "n":n,
                "monthly_emi":monthly_emi,
                "total_ammount":total_ammount,
                "total_interest":interest,
                "n":n,
            }
            return render(request,"app1/1.html",context)
        
    else:
        form=form1()
    return render(request,"app1/1.html",{"form":form})

def view2(request):
    data=model1.objects.all()
    return render(request,"app1/2.html",{"data":data})
    
