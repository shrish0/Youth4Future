from django.shortcuts import render
from .models import *
# Create your views here.
from django.conf import settings
from django.http import HttpResponse


def home(request):
    return render(request,"pages\index.html")



def contacts(request):
    return render(request,"pages\contacts.html")


def courses(request):
    return render(request,"pages\courses.html")

def blog(request):
    return render(request,"pages\courses.html")

def about(request):
    return render(request,"pages\\about.html")

def courses_detail(request):
    return render(request,"pages\course-details.html")

def subject_detail(request):
    return render(request,"pages\subject_details.html")

def FaQ(request):
    return render(request, 'pages\FaQ.html')
