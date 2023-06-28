from django import forms

class CrearClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=10)
    apellido = forms.CharField(max_length=10)
    edad = forms.IntegerField()
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField(required=False)
