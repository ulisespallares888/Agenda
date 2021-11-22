from typing import Text
from django.db import models
from django.contrib.auth.models import User

class notitas(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    propietario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        salida = '{0} {1} {2}'
        return salida.format(self.titulo,self.contenido,self.propietario)

