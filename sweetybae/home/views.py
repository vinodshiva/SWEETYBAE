from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User


def index(request):
    return render(request,"index.html")

def text(request):
    return render(request,"text.html")

def login(request):
    return render(request,"login.html")
def register(request):
    return render(request,"register.html")

def logsub(request):
    uname=request.POST["uname"]
    pname=request.POST["pname"]
    user=auth.authenticate(username=uname,password=pname)
    if user:
        auth.login(request,user)
        return redirect('/')
    return render(request,"login.html",{'val':uname})



def regsub(request):
    uname=request.POST["uname"]
    pname=request.POST["pname"]
    bname=request.POST["bname"]
    aname=request.POST["aname"]
    pwname=request.POST["pwname"]
    rpwname=request.POST["rpwname"]
    if pwname==rpwname:
        if User.objects.filter(username=bname):
            msg="username is already taken"
            return render(request,"text.html",{'val':msg})
        elif User.objects.filter(email=aname):
            msg="email is already taken"
            return render(request,"text.html",{'val':msg})
        else:
            user=User.objects.create_user(first_name=uname,last_name=pname,username=bname,email=aname,password=pwname)
            user.save();
            return redirect('/')
    else:
        msg="password do not match"
    return render(request,"text.html",{'val':msg})



# Create your views here.
