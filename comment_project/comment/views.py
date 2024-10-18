from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.template import loader
from .models import ContactUs
from .forms import contactusModel
import socket
# Create your views here.

"""
def home(request):
    page=loader.get_template("../templates/listUser.html")
    result=User.objects.all()
    context={"model":result}
    return HttpResponse(page.render(context))
"""

"""
def listUser(request):
    page2=loader.get_template("../templates/index.html")
    result2=User.objects.filter(Id=2).first()
    context={"model":result2}
    return HttpResponse(page.render(context))
"""
"""
def listusers(request):
    page2=loader.get_template("../templates/index.html")
    result2=User.objects.all()
    context={"model":result2}
    return HttpResponse(page2.render(context))
"""

def contactUss(request):
    msg=""
    hostname=socket.gethostname()
    ip_address=socket.gethostbyname(hostname)
    print(ip_address)
    if request.method=="POST":
        forms = contactusModel(request.POST)
        if forms.is_valid():
            result=ContactUs(Fullname=forms.data["Fullname"],Email=forms.data["Email"],message=forms.data["message"] ,Ip=ip_address)
            result.save()
            msg="ثبت شد"



    forms = contactusModel()
    return render(request=request, template_name="ContactUs.html", context={"form": forms})

def savecontact(request):
    if request.method=="POST":
        forms = contactusModel(request.POST)

def mycomment(request):
    hostname=socket.gethostname()
    ip_address=socket.gethostbyname(hostname)
    MyCommentList = ContactUs.objects.filter(TrueOrFalse="True").all()
    return render(request=request, template_name="MyComment.html", context={"MyCommentList": MyCommentList})

def EditCotaxt(request,id):
    result=ContactUs.objects.filter(Id=id).first()
    msg=""
    action="/EditSave"
    forms=contactusModel(initial={"Id" : id,"Fullname" : result.Fullname , "Email" : result.Email ,"message" : result.message})
    return render(request=request, template_name="ContactUs.html", context={"form": forms, "action":action})

def EditSave(request):
    if request.method=="POST":
        forms=contactusModel(request.POST)
        id=forms.data["Id"]
        result = ContactUs.objects.filter(Id=id).first()
        result.Fullname=forms.data["Fullname"]
        result.Email=forms.data["Email"]
        result.message=forms.data["message"]
        result.save()
        return HttpResponseRedirect("/mycomment")


def DeleteCotaxt(request,id):
    result = ContactUs.objects.filter(Id=id).first()
    result.delete()
    return HttpResponseRedirect("/mycomment")