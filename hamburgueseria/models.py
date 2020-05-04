from django.db import models


class Ingrediente(models.Model):
    id = models.IntegerField
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre

class Hamburguesa(models.Model):
    id = models.IntegerField
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField(default=0, editable=True)
    descripcion = models.CharField(max_length=60)
    imagen = models.CharField(max_length=200)
    ingredientes_hamburguesa = models.ManyToManyField(Ingrediente)
    def __str__(self):
        return self.nombre