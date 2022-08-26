from django.db import models

# Create your models here.
class Domicilio(models.Model):
    calle = models.CharField(max_length=50)
    numero = models.IntegerField()
    ciudad = models.CharField(max_length=50)

    def __str__(self):
        return f'Domicilio {self.id} -- Calle: {self.calle} | Numero: {self.numero} | Ciudad: {self.ciudad}'

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'Persona {self.id} -- Nombre: {self.nombre} | Apellido: {self.apellido} | Edad: {self.edad}'