from django.db import models

class User(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=20)
    usuario = models.CharField(max_length=30)
    contrasena = models.CharField(max_length=30, null=True)


    def __str__(self):
        return self.usuario