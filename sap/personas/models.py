from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()

    def __str__(self):
        return f'Persona {self.id} -- Nombre: {self.nombre} | Apellido: {self.apellido} | Edad: {self.edad}'