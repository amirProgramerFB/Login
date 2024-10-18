from django.db import models

"""
class User(models.Model):
    Id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    family=models.CharField(max_length=250)
    age=models.IntegerField(null=False)
"""


class ContactUs(models.Model):
    Id = models.AutoField(primary_key=True)
    Fullname=models.CharField(max_length=200,verbose_name="نام کامل" )
    Ip=models.CharField(max_length=100,null=True,verbose_name="آیپی")
    TrueOrFalse=models.CharField(max_length=100,null=True,verbose_name="تاییدی")
    Email=models.CharField(max_length=250 ,verbose_name="ایمیل")
    message=models.TextField(max_length=255,verbose_name="متن پیام")

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"

