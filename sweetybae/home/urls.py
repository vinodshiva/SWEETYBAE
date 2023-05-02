from . import views
from django.urls import path
urlpatterns = [
    path ('',views.index),
    path ("xyz/",views.text),
    path ("login/",views.login,name="loginpage"),
    path ("raja/",views.register,name='registerpage'),
    path ("logout/",views.logout)
   
]
