from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login',views.Login,name="فرم ورود "),
    path('REGISTER',views.REGISTER,name="فرم ورود "),
    path('chekLogin',views.chekLogin,name="فرم ورود "),



]