from django.db import models

# Create your models here.

class ContactData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " - " + self.email
    
class CourseDetail(models.Model):
    className=models.CharField(max_length=50,default="")
    courseName = models.CharField(max_length=100)
    chapter = models.CharField(max_length=100)
    video = models.TextField()
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.className + " - " + self.courseName
    
class Blogs(models.Model):
    topic=models.CharField(max_length=50)
    link=models.TextField()
    subject=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.topic + " " + self.created_at
