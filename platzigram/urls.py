""" Creacion de hola mundo en Django"""
from django.urls import path
from django.http import HttpResponse

def hello_world(request):
    """Funcion hello_world retorna una http"""
    return HttpResponse("Hello world")

urlpatterns = [
    path('hello-world', hello_world)
]
