from django.db import models

class User(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    usuario = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.usuario
