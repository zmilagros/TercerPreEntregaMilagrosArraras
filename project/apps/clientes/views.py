from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm

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
    return render(request, "clientes/about.html",context)