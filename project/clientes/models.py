from django.db import models
# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
