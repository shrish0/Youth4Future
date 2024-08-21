from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import  login as login_auth
from django.contrib.auth.models import  auth
from django.contrib.auth.hashers import make_password
from .form import *
# Create your views here.
from django.contrib.auth import get_user_model
User = get_user_model()
def logout(request):
    auth.logout(request)
    return redirect("/")

def login(request):
    if request.method == "POST" :
        username=request.POST["username"]
        password1=request.POST["password"]
        user=auth.authenticate(username=username,password=password1)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid Credential")
            return redirect("login")
    return render(request,"login.html")

def register(request):
    if request.method == "POST":
        form = SignupForm(request.POST)  # Assign the form instantiation to a variable
        if form.is_valid():
            form.save()
            return render(request, "login.html")
    else:
        form = SignupForm()
    return render(request, "signup.html", {'form': form})
    
# def register(request):
#     if request.method == "POST" :
#        form.SignupForm(request.POST)
#        if form.is_valid():
#             form.save()
#             return render(request,"login.html")
#     form=SignupForm()
#     return render(request,"register.html",{'form':form})
#     */
def home(request):
    return redirect("/")