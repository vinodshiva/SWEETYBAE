from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from product.models import fruits


def index(request):
    obj=fruits.objects.all()
    if 'username' in request.COOKIES:
        name=request.COOKIES['username']
    else:
        name=''
    print("hiiiii",obj)
    return render(request,"index.html",{'data':obj,'name':name})
def text(request):
    return render(request,"text.html")


def login(request):
    if request.method=="POST":
            uname=request.POST["uname"]
            pname=request.POST["pname"]
            user=auth.authenticate(username=uname,password=pname)
            if user:
                auth.login(request,user)
                res=redirect('/')
                res.set_cookie("username",uname)
                return res
            msg= "invalid username and password"
            return render(request,"login.html",{'msg':msg})
    else:
        return render(request,"login.html")


def register(request):
    if request.method=='POST':
        uname=request.POST["uname"]
        pname=request.POST["pname"]
        bname=request.POST["bname"]
        aname=request.POST["aname"]
        pwname=request.POST["pwname"]
        rpwname=request.POST["rpwname"]
        if pwname==rpwname:
            if User.objects.filter(username=bname):
                msg="username is already taken"
                return render(request,"register.html",{'msg':msg})
            elif User.objects.filter(email=aname):
                msg="email is already taken"
                return render(request,"register.html",{'msg':msg})
            else:
                user=User.objects.create_user(first_name=uname,last_name=pname,username=bname,email=aname,password=pwname)
                user.save();
                auth.login(request,user)
                return redirect('/')
        else:
            msg="password do not match"
        return render(request,"register.html",{'msg':msg})
    else:
        return render(request,"register.html")


def logout(request):
    auth.logout(request)
    lg=redirect("/")
    lg.delete_cookie('username')
    return lg




# Create your views here.
