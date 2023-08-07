from django.shortcuts import render
from .models import Categoria
from django.http import HttpResponse, HttpRequest


def inicioTienda(request):
    return render(request, "TIENDA/index.html")


def categorias(request):
    categorias = Categoria.CATEGORIAS
    categorias_filas = [categorias[i:i+5] for i in range(0, len(categorias), 5)]
    return render(request, "TIENDA/store.html", {'categorias_filas': categorias_filas})






