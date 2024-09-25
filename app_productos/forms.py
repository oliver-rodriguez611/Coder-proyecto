from django import forms

class PlatosFormulario(forms.Form):

    plato =forms.CharField()
    precio = forms.IntegerField()