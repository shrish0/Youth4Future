from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('index', views.home, name='index'),
    path("contacts", views.contacts, name="contacts"),
    path("courses", views.courses, name="courses"),
    path("blog", views.blog, name="blog"),
    path("aboutus", views.about, name="about"),
    path("FaQ", views.FaQ, name="FaQ"),
    path("course-details", views.courses_detail, name="course-details"),
]
