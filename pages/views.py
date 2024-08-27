from django.contrib import messages
from django.shortcuts import render , redirect
from .models import *
# Create your views here.
from django.http import JsonResponse
from django.conf import settings
from django.http import HttpResponse


def home(request):
    return render(request,"pages\index.html")


# views.py

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        contact = ContactData(name=name, email=email, subject=subject, message=message)
        contact.save()
        
        # Add a success message
        messages.success(request, "Your message has been sent. Our team will contact you shortly.")
        
        # Redirect to the same page to show the message
        return redirect('contacts')
    
    return render(request, "pages/contacts.html")



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
    qna_data = [
        {"question": "Where can I find the bot?", "answer": "You can find it on our site under downloads."},
        {"question": "How do I install the app?", "answer": "You can download the installer from our website and follow the installation instructions."},
        {"question": "Can a normal person also use this site ", "answer": "Yes ,anyone can acess it but for the specially abled bot is given."},
        {"question": "What Type of courses offer", "answer": "Generally of class 10 , 12 and some coding language"},
        {"question": "Future plan ", "answer": "Generally of class 10 , 12 and some coding language"},
        # Add more Q&A pairs as needed
    ]
    return render(request, 'pages\FaQ.html', {'qna_data': qna_data})
