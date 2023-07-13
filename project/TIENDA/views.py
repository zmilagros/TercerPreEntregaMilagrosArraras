from django.shortcuts import render
from .models import Cliente, Producto, Categoria
from django.http import HttpResponse, HttpRequest
from .forms import ProductoForm, ClienteForm


def inicioTienda(request):
    return render(request, "TIENDA/inicio.html")

def clientes(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = Cliente()
            cliente.nombre = form.cleaned_data['nombre']
            cliente.apellido = form.cleaned_data['apellido']
            cliente.email = form.cleaned_data['email']

            cliente.save()
            form = ClienteForm()
    else:
        form = ClienteForm()

    clientes = Cliente.objects.all()
    context={"clientes":clientes, "form":form}
    return render(request, "TIENDA/clientes.html",context)

def productos(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = Producto()
            producto.descripcion = form.cleaned_data['descripcion']
            producto.talle = form.cleaned_data['talle']
            producto.precio = form.cleaned_data['precio']
            producto.save()
            form  = ProductoForm()
    else:
        form = ProductoForm()


    productos = Producto.objects.all()
    context={"productos":productos, "form":form}
    return render(request, "TIENDA/productos.html",context)

def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias.html', {'categorias': categorias})


