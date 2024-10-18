from django.db import models

# Create your models here.


class SingIn(models.Model):
    Id = models.AutoField(primary_key=True)
    Ip=models.CharField(max_length=100,null=True,verbose_name="آیپی")
    name=models.CharField(max_length=200,verbose_name="name" )
    Email=models.CharField(max_length=200,verbose_name="Email" )
    Password=models.CharField(max_length=255,verbose_name="Password")


class LogIn(models.Model):
    Id = models.AutoField(primary_key=True)
    Ip=models.CharField(max_length=100,null=True,verbose_name="آیپی")
    Email=models.CharField(max_length=200,verbose_name="Email" )
    Password=models.CharField(max_length=255,verbose_name="Password")



