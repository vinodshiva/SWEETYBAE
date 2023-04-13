from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def text(request):
    return render(request,"text.html")


# Create your views here.
