from django.db import models

class Producto(models.Model):
    descripcion=models.CharField(max_length=50)
    talle=models.CharField(max_length=50, default="")
    precio=models.FloatField()

    def __str__(self):
        return f" Descripción: {self.descripcion} - Talle: {self.talle} - Precio: {self.precio}"
    
