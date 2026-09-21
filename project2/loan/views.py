from django.shortcuts import render
from .forms import form1

def view1(request):
    if request.method=="POST":
        form=form1(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            address=form.cleaned_data['address']
            account_number=form.cleaned_data['account_number']

            context={
                'name':name,
                'address':address,
                'account_number':account_number,
            }
            return render(request,'loan/1.html',context)
    else:

        form=form1()
        return render(request,'loan/1.html',{'form':form})

# Create your views here.
