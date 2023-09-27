from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone


class usuarios(models.Model):
    usuario = models.ForeignKey(User, verbose_name=(""), on_delete=models.DO_NOTHING)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField( max_length=50)
    dni = models.IntegerField()

class alarma(models.Model):
    horaentrada = models.DateTimeField(default=timezone.now)
    horasalida = models.DateTimeField(blank=True, null=True)
    activa = models.BooleanField(default=True, blank=True, null=True)
    

class formulario(models.Model):
    nombre = models.CharField( max_length=50)
    apellido = models.CharField( max_length=50)
    dni = models.IntegerField()
    motivoingreso = models.TextField(max_length=400)
    horaentrada = models.DateTimeField()
    horasalida = models.DateTimeField(blank=True, null=True)

class habitacion(models.Model):

    camas = models.IntegerField()
    piso = models.IntegerField()
    numero = models.IntegerField()

class cama(models.Model):
    numero = models.IntegerField()
    ocupada = models.BooleanField()
    paciente = models.CharField(null=True, blank=True, max_length=50)
    habitacion = models.IntegerField()

def __str__(self):
    return self.nombre




# Create your models here.


