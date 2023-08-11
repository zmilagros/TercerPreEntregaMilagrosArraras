from django.db import models

class Producto(models.Model):
    descripcion = models.CharField(max_length=50)
    talle = models.CharField(max_length=50, default="")
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)  # Agrega este campo

    def __str__(self):
        return f"Descripción: {self.descripcion} - Talle: {self.talle} - Precio: {self.precio}"
