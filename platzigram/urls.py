""" Creacion de hola mundo en Django"""
from django.urls import path
from platzigram import views

urlpatterns = [
    path('hello-world', views.hello_world)
]
