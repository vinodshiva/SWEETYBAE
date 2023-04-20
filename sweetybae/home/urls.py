from . import views
from django.urls import path
urlpatterns = [
    path ('',views.index),
    path ("xyz/",views.text),
    path ("login/",views.login),
    path ('login/loginsub/',views.logsub),
    path ("raja/",views.register),
    path ('raja/registersub/',views.regsub),
]
