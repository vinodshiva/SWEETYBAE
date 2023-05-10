from django.shortcuts import render,redirect
from .models import fruits,comment
def details(request):
    iname=request.GET['id']
    obj=fruits.objects.get(id=iname)
    return render(request,"about.html",{'fruit':obj})
def cmt(request):
    imsg=request.GET["cmtmsg"]
    ipro=request.GET["proid"]
    iuser=request.GET["user"]

    obj=comment.objects.create(msg=imsg,user=iuser,proid_id=ipro,like=0)
    obj.save()
    return redirect("/product/?id="+ipro)

def like(request):
    return render(request,"text.html")


# Create your views here.
