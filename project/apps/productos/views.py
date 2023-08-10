from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from .models import Producto
from .forms import ProductoForm


class ProductoList(ListView):
    model = Producto
    template_name = "productos/products.html"
    context_object_name = "productos"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProductoForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = Producto(
                descripcion=form.cleaned_data['descripcion'],
                talle=form.cleaned_data['talle'],
                precio=form.cleaned_data['precio']
            )
            producto.save()
            form = ProductoForm()
        else:
            form = ProductoForm()

        productos = self.model.objects.all()
        context = {"productos": productos, "form": form}
        return self.render_to_response(context)


@method_decorator(login_required(login_url=reverse_lazy('clientes:usuarios-login')), name='dispatch')    
class ProductoCreate(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "productos/crearproducto.html"
    success_url = reverse_lazy("productos:lista_productos")



class ProductoDetail(DetailView):
    template_name = "productos/detalleproducto.html"
    model = Producto


@method_decorator(login_required(login_url=reverse_lazy('clientes:usuarios-login')), name='dispatch')
class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = "productos/crearproducto.html"
    success_url = reverse_lazy("productos:lista_productos")


@method_decorator(login_required(login_url=reverse_lazy('clientes:usuarios-login')), name='dispatch')
class ProductoDelete(DeleteView):
    model = Producto
    template_name = "productos/eliminarproducto.html"
    success_url = reverse_lazy("productos:lista_productos")
