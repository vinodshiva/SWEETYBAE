from django.shortcuts import render
from .models import fruits 
def details(request):
    iname=request.GET['id']
    obj=fruits.objects.get(id=iname)
    return render(request,"about.html",{'fruit':obj})
def cmt(request):
    return render(request,"text.html")
def like(request):
    return render(request,"text.html")


# Create your views here.
