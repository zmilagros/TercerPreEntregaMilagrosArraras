from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

    
class Producto(models.Model):
    descripción=models.CharField(max_length=50)
    talle=models.CharField(max_length=50, default="")
    precio=models.FloatField()

    def __str__(self) -> str:
        return f"Descripción: {self.descripción} - Talle: {self.talle} - Precio: {self.precio}"
    

class Categoria(models.Model):
    CATEGORIA = [
        ('partesuperior', 'tops y remeras'),
        ('parteinferior', 'faldas y pantalones'),
        ('cuerpoentero', 'vestidos y enterizos'),
        ('segundapiel', 'abrigos y buzos'),
        ('ropainterior', 'ropa interior')
    ]

    nombre=models.CharField(max_length=50, choices=CATEGORIA)

    def __str__(self) -> str:
        return self.nombre

