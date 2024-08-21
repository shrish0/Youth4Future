from . import views
from django.urls import path
from . import views

urlpatterns = [
    
    path("login.html",views.login,name="login"),
    path("login",views.login,name="login"),
    path("signup",views.register,name="register"),
    path("signup.html",views.register,name="register"),
    path("logout",views.logout,name="logout"),
    path("logout.html",views.logout,name="logout"),
    path("index.html",views.home,name="index"),


]