from django.db import models
from productos.models import Producto


class Categoria(models.Model):
    CATEGORIAS = [
        ('partesuperior', 'Blusas y Camisas'),
        ('parteinferior', 'Pantalones y Faldas'),
        ('cuerpoentero', 'Vestidos y Enterizos'),
        ('segundapiel', 'Abrigos'),
        ('ropa de cama', 'Pijamas')
    ]

    nombre = models.CharField(max_length=50, choices=CATEGORIAS)

    def __str__(self):
        return self.nombre


