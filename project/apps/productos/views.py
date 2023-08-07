from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

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
    return render(request, "productos/products.html",context)
