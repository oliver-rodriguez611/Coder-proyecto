from django.db import models

# Create your models here.
#curso
class Plato(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self):
        return f'{self.nombre}'

    class Meta():

        verbose_name = 'Platos'
        verbose_name_plural = 'Nuestros Platos'

#estudiantes en el video
class clientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nombre} - {self.apellido}'
    
    class Meta():

        verbose_name = 'Clientes'
        verbose_name_plural = 'Nuestros Clientes'




class empleados(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    identificacion = models.IntegerField()
    email = models.EmailField()
    cargo = models.CharField(max_length=50, null = True)

    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.identificacion}'
    
    class Meta():

        verbose_name = 'Talento Humano'
        verbose_name_plural = 'Nuestros Colaboradores'





