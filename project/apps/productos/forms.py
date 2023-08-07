from django import forms

class ProductoForm(forms.Form):
    descripcion=forms.CharField(max_length=50)
    talle=forms.CharField(max_length=50)
    precio=forms.FloatField()