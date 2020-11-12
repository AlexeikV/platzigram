"""Creacion de vistas para consumo del portal"""
"""Django"""
from django.http import HttpResponse

"""Utilidades"""
from datetime import datetime

def hello_world(request):
    """Funcion hello_world retorna una http"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh hi!, the current time is {now}'.format
                        (now=now)
                        )