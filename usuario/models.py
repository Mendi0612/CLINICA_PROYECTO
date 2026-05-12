from django.db import models

class Usuario(models.Model):

    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    documento = models.CharField(max_length=30, unique=True)
    correo = models.EmailField(unique=True)
    edad = models.IntegerField()
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.nombre

 