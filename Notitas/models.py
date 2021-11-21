from typing import Text
from django.db import models
from django.contrib.auth.models import User

class notitas(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    continido = models.TextField()
    fecha = models.DateField()
    propietario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        salida = '{0} {1} {2} {3} {4}'
        return salida.format(self.titulo,self.descripcion,self.continido,self.fecha,self.propietario)

