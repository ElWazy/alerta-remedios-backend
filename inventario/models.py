from django.db import models


class Remedio(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=19, decimal_places=4)
    descripcion = models.TextField(null=True)
    fecha_vencimiento = models.DateTimeField()
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
