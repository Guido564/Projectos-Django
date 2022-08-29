from django.http import HttpResponse
from django.shortcuts import render

from personas.models import Persona, Domicilio


# Create your views here.
def bienvenido(request):
    personas_total = Persona.objects.all()
    no_personas = Persona.objects.count()

    return render(request, 'bienvenido.html', {'no_personas': no_personas, 'personas_total': personas_total})


def domicilio(request):
    domiclios_total = Domicilio.objects.all()
    domicilios_nro = Domicilio.objects.count()

    return render(request, 'domicilios.html', {'domicilios_nro': domicilios_nro, 'domiclios_total': domiclios_total})
