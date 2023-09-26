from django.db import models
from django.contrib.auth.models import User


class usuarios(models.Model):
    usuario = models.ForeignKey(User, verbose_name=(""), on_delete=models.DO_NOTHING)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField( max_length=50)
    dni = models.IntegerField(max_length=50)
    medico = models.CharField(max_length=50)


class medico(models.Model):
    nombre = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dni = models.IntegerField(max_length=30)



class alarma(models.Model):
    horaentrada = models.DateTimeField()
    horasalida = models.DateTimeField(blank=True, null=True)
    activa = models.BooleanField(default=True, blank=True, null=True)
    

class formulario(models.Model):

    horaentrada = models.DateTimeField()
    horasalida = models.DateTimeField(blank=True, null=True)

class habitacion(models.Model):

    piso = models.IntegerField(max_length=4)
    numero = models.IntegerField(max_length=4)
    camas = models.IntegerField(max_length=4)

class cama(models.Model):
    numero = models.IntegerField()
    ocupada = models.BooleanField()
    paciente = models.IntegerField()






# Create your models here.


