from django.db import models
from clientes.models import Cliente
from productos.models import Producto

# Create your models here.


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


