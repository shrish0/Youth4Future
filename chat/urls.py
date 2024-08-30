from django.urls import path
from .views import *

urlpatterns = [
     path('', choose_group, name='choose_group'),
    path('<str:group_name>/', chat, name='chat'),
    path('<str:group_name>/send_message/', send_message, name='send_message'),
    path('<str:group_name>/get_messages', get_message , name='get_messages'),
    path("back",home,name="index"),
    path("<str:group_name>/back",back,name="Group_change")
]
