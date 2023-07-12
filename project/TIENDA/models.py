from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    
class Producto(models.Model):
    descripción=models.CharField(max_length=50)
    talle=models.CharField(max_length=50, default="")
    precio=models.FloatField()

    def __str__(self):
        return f"Descripción: {self.descripción} - Talle: {self.talle} - Precio: {self.precio}"
    

class Categoria(models.Model):
    CATEGORIAS = [
        ('parte-superior', 'Tops y Remeras'),
        ('parte-inferior', 'Faldas y Pantalones'),
        ('cuerpo-entero', 'Vestidos y Enterizos'),
        ('segunda-piel', 'Abrigos y Buzos'),
        ('ropa-interior', 'Ropa Interior')
    ]

    nombre = models.CharField(max_length=50, choices=CATEGORIAS)

    def __str__(self):
        return self.nombre


