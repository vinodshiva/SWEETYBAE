from . import views
from django.urls import path
from.feed import latest

urlpatterns = [
    path ('',views.index, name='homepage'),
    path ("xyz/",views.text),
    path ("login/",views.login,name="loginpage"),
    path ("raja/",views.register,name='registerpage'),
    path ("logout/",views.logout),
    path('feed/',latest()),

   
]
