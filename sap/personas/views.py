from django.shortcuts import render

from personas.models import Persona


# Create your views here.
def detallePersonas(request, id):
    persona = Persona.objects.get(pk=id)
    return render(request, 'personas/detalle.html', {'persona': persona})
