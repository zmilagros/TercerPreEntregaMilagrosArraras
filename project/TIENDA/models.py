from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    
class Producto(models.Model):
    descripcion=models.CharField(max_length=50)
    talle=models.CharField(max_length=50, default="")
    precio=models.FloatField()

    def __str__(self):
        return f" Descripción: {self.descripcion} - Talle: {self.talle} - Precio: {self.precio}"
    


class Categoria(models.Model):
    CATEGORIAS = [
        ('partesuperior', 'Tops y Remeras'),
        ('parteinferior', 'Pantalones y Faldas'),
        ('cuerpoentero', 'Vestidos y Enterizos'),
        ('segundapiel', 'Abrigos y Buzos'),
        ('ropainterior', 'Ropa Interior')
    ]

    nombre = models.CharField(max_length=50, choices=CATEGORIAS)

    def __str__(self):
        return self.nombre


