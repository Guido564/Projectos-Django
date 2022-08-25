from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request):
    return HttpResponse('Hola mundo desde Django')

def despedirse(request):
    return HttpResponse('Nos vemos desde Django')

def contacto(request):
    return HttpResponse('Mail: guidopruzzo564@gmail.com | Telefono: telefonofalso123')
