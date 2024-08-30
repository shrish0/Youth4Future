from django.db import models
from account.models import User 

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    group_number = models.TextField()
