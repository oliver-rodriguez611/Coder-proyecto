from django import forms

class PlatosFormulario(forms.Form):

    plato =forms.CharField()
    precio = forms.IntegerField()

class ClientesFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class EmpleadosFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    identificacion = forms.IntegerField()
    email = forms.EmailField()
    cargo = forms.CharField()
    