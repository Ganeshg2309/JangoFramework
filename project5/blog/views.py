from django.shortcuts import render,redirect,get_object_or_404
from .models import post
from .forms import postform

def home(request):
    posts=post.objects.all()
    return render(request,"blog/1.html",{"posts":posts})

def post_detail(request,id):
    posts=get_object_or_404(post,id=id)
    return render(request,"blog/2.html",{"posts":posts})

def create_post(request):
    
    if request.method=="POST":
        form=postform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
            

    else:
        form=postform()
    return render(request,"blog/3.html",{"form":form})

def edit_post(request,id):
    post1=get_object_or_404(post,id=id)
    if request.method=="POST":
        form=postform(request.POST,instance=post1)
        if form.is_valid():
            form.save()
            return redirect('post_detail',id=id)
    else:
        form=postform(instance=post1)
    return render(request,"blog/4.html",{"form":form})

def delete_post(request,id):
    post1=get_object_or_404(post,id=id)
    if request.method=="POST":
        post1.delete()
        return redirect('home')
    return render(request,"blog/5.html",{"posts":post1})
