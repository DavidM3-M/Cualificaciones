from django.db import models

# Create your models here.

class Person(models.Model):
    nro_de_cedula = models.CharField(max_length=20)
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=20)
    pais_de_residencia = models.CharField(max_length=20)
    departamento_de_residencia = models.CharField(max_length=20)
    ciudad_de_residencia = models.CharField(max_length=50)
    barrio_de_residencia = models.CharField(max_length=20)
    direccion_de_residencia = models.CharField(max_length=100)

    def __str__(self):
        return self.nro_de_cedula


   


