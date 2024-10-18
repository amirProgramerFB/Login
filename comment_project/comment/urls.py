from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.contactUss,name="فرم"),
    path('mycomment',views.mycomment,name="لیست کامنت ها"),
    path('EditSave',views.EditSave,name="لیست کامنت ها"),
    path('EditCotaxt/<int:id>',views.EditCotaxt,name="لیست کامنت ها"),
    path('DeleteCotaxt/<int:id>',views.DeleteCotaxt,name="لیست کامنت ها"),
    path('savecontact',views.savecontact,name="لیست کامنت ها"),


]