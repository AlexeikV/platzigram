"""Creacion de vistas para consumo del portal"""
"""Django"""
from django.http import HttpResponse

"""Utilidades"""
from datetime import datetime
import json

def hello_world(request):
    """Funcion hello_world retorna una http"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh hi!, the current time is {now}'.format
                        (now=now)
                        )

def sort_integers(request):
    """Return a JSON response with sorted integers."""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully.'
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )

def say_hi(request, name, age):
    """Return a greeting."""
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}: Welcome to Platzigram'.format(name)
    return HttpResponse(message)