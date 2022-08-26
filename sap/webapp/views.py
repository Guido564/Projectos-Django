from django.http import HttpResponse
from django.shortcuts import render

from personas.models import Persona


# Create your views here.
def bienvenido(request):
    personas_total = Persona.objects.all()
    no_personas = Persona.objects.count()

    return render(request, 'bienvenido.html', {'no_personas': no_personas, 'personas_total': personas_total})

