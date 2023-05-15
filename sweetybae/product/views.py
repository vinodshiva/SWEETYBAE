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
    cmtid=request.GET['id']
    obj=comment.objects.filter(id=cmtid)
    like=int(obj[0].like)+1
    obj.update(like=str(like))
    return redirect("/product/?id="+str(obj[0].proid_id))
    


# Create your views here.
