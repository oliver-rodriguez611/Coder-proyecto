from django.db import models

# Create your models here.
class Plato(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()

#estudiantes en el video
class clientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

#profesor en el video
class empleados(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    identificacion = models.IntegerField()
    email = models.EmailField()
    cargo = models.CharField(max_length=50, null = True)





