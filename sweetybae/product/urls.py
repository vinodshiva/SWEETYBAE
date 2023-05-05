from .import views
from django.urls import path

urlpatterns = [
path ('',views.details),
path ('cmt',views.cmt),
path ('like',views.like),

]