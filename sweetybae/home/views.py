from django.shortcuts import render,redirect
from django.contrib import auth
def index(request):
    return render(request,"index.html")

def text(request):
    return render(request,"text.html")

def login(request):
    return render(request,"login.html")
def register(request):
    return render(request,"register.html")

def logsub(request):
    uname=request.GET["uname"]
    pname=request.GET["pname"]
    user=auth.authenticate(username=uname,password=pname)
    if user:
        auth.login(request,user)
        return redirect('/')
    return render(request,"text.html",{'val':uname})



def regsub(request):
    uname=request.GET["uname"]
    pname=request.GET["pname"]
    # aname=request.GET["aname"]
    # bname=request.GET["bname"]
    # cname=request.GET["cname"]
    return render(request,"text.html",{'val':uname,'val2':pname})



# Create your views here.
