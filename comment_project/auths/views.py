from django.template import loader
from django.shortcuts import render
from .forms import LOIGIN,Register
from .models import LogIn
import socket
from django.contrib.auth import authenticate,login
from django.http import HttpResponse , HttpResponseRedirect

# Create your views here.


def Login(request):
    forms = LOIGIN()
    return render(request=request, template_name="login.html", context={"form": forms})

def savecontact(request):
    if request.method=="POST":
        forms = LOIGIN(request.POST)


def REGISTER(request):
    forms=Register()
    return render(request=request, template_name="SingUp.html", context={"form": forms})



def chekLogin(request):
    if request.method == 'POST':
        form = LOIGIN(request.POST)
        if form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(request, email=email, password=password)
            login(request, user )
            return HttpResponse('ghghgh')
        else:
            form = LOIGIN()
            return render(request, 'templates/links1.html', {'form': request(form)})




