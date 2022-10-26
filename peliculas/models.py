from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Genero(models.Model):
    nombre = models.CharField(max_length=64, help_text="Pon el nombre del genero")

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo = models.CharField(max_length=50)
    director = models.ForeignKey("Director", on_delete=models.SET_NULL, null=True)#estoy relacionando esta tabla
    descipcion = models.TextField(max_length=300, help_text="Pon aqui una descipcion de la pelicula ")
    genero = models.ManyToManyField(Genero)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return  reverse('detalle de la pelicula', args=[str(self.id)])

class Director(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_de_nacimiento = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('detalle del director', args=[str(self.id)])

    def __str__(self):
        return '%s (%s)' % (self.apellido, self.nombre)
