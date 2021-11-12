from django.db import models
from django.contrib.auth.models import User

class usuario(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length = 50)

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.nombre)

class contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.IntegerField()
    email = models.EmailField(max_length = 254)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        cadena = "{0} {1} {2} {3} {4}"
        return cadena.format(self.nombre,self.apellido,self.telefono,self.email,self.usuario)

