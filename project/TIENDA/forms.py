from django import forms

class ClienteForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()

class ProductoForm(forms.Form):
    descripcion=forms.CharField(max_length=50)
    talle=forms.CharField(max_length=50)
    precio=forms.FloatField()