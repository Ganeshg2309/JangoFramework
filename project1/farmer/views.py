from django.shortcuts import render

def view1(request):
    name="ramesh"
    address="mysore"
    account_number="22445566"

    context={
        "name": name,
        "address":address,
        "account_number":account_number
    }
    return render(request,"farmer/1.html",context)

# Create your views here.
