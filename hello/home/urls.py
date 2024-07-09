from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index,name="index"),
    path('contact', views.contact,name="contact"),
    path('about', views.about,name="about"),
    path('services', views.services,name="services") ,
    path('home', views.home,name="home")
]
