from django.shortcuts import render, redirect
from .models import Producto
from django.urls import reverse_lazy
from .forms import ProductoForm
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import forms, models

class ProductoList(ListView):
    model = Producto
    template_name = "productos/products.html"
    context_object_name = "productos"
    form_class = ProductoForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            producto = Producto()
            producto.descripcion = form.cleaned_data['descripcion']
            producto.talle = form.cleaned_data['talle']
            producto.precio = form.cleaned_data['precio']
            producto.save()
            form = self.form_class()
        else:
            form = self.form_class()

        productos = self.model.objects.all()
        context = {"productos": productos, "form": form}
        return self.render_to_response(context)
    

class ProductoCreate(CreateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("productos:productos")

class ProductoDetail(DetailView):
    model = models.Producto

class ProductoUpdate(UpdateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("productos:productos")

class ProductoDelete(DeleteView):
    model = models.Producto
    success_url = reverse_lazy("productos:productos")

