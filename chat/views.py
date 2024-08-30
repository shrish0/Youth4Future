from django.shortcuts import render, redirect
from .models import Message
from django.contrib.auth.decorators import login_required
from django.templatetags.static import static

@login_required
def chat(request, group_name):
    if group_name in ["farmer","small-retailer","global"] :
       messages = Message.objects.filter(group_number=group_name).order_by('-timestamp')
       return render(request, 'chat/chat.html', {'messages': messages, 'group_number': group_name})
    else :
       return redirect('choose_group')

@login_required
def send_message(request, group_name):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            message = Message.objects.create(sender=request.user, group_number=group_name, content=content)
    return redirect('chat', group_name=group_name)


@login_required
def choose_group(request):
    # Logic to fetch available group numbers or generate a list of available groups
    available_groups = ["FARMER", "LOCAL SELLER", "GLOBAL"]
    available_images = [
        static('images/channel1.jpeg'),
        static('images/channel2.png'),
        static('images/channel3.png'),
    ]
    available_description = ["Communication Channel for Farmers - A specialized communication channel designed for farmers to exchange vital information related to agriculture and farming practices",  "Communication Channel for Personal Conversations - This communication channel is tailored for individuals seeking a private space to engage in one-on-one conversations. Whether for personal or professional purposes", "Global Communication Channel - A universal communication channel that transcends geographical boundaries, enabling people from around the globe to connect and converse in a shared online space"]
    available_link=["farmer","small-retailer","global"]
    # Combine group names and corresponding image paths
    groups_with_images = zip(available_groups, available_images, available_description,available_link)
    return render(request, 'chat/choose_group.html', {'groups_with_images': groups_with_images})

@login_required
def get_message(request,group_name):
    if group_name in ["farmer","small-retailer","global"] :
       messages = Message.objects.filter(group_number=group_name).order_by('-timestamp')
       return render(request, 'chat/chat_box.html', {'messages': messages, 'group_name': group_name})

def home(request):
    return redirect("/")

def back(request,group_name):
    return redirect("/chat")
