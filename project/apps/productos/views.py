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

@method_decorator(login_required, name='dispatch')
class ProductoList(ListView):
    model = Producto
    template_name = "productos/products.html"
    context_object_name = "productos"
    form_class = ProductoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProductoForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            form = self.form_class()
        else:
            form = self.form_class()

        productos = self.model.objects.all()
        context = {"productos": productos, "form": form}
        return self.render_to_response(context)

class ProductoCreate(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "productos/crearproducto.html"
    success_url = reverse_lazy("productos:lista_productos")

class ProductoDetail(DetailView):
    template_name = "productos/detalleproducto.html"
    model = Producto

class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = "productos/crearproducto.html"
    success_url = reverse_lazy("productos:lista_productos")

class ProductoDelete(DeleteView):
    model = Producto
    template_name = "productos/eliminarproducto.html"
    success_url = reverse_lazy("productos:lista_productos")
