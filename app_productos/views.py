from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import PlatosFormulario

# Create your views here.

def agrega_plato(req, nombre, precio):

    nuevo_plato = Plato(nombre = nombre, precio = precio)
    nuevo_plato.save()

    return HttpResponse(f"""
        <p>Plato: {nuevo_plato.nombre} - precio {nuevo_plato.precio} creado con exito!<p>
    """)

def lista_platos(req):

    lista = Plato.objects.all()

    return render(req, "lista_platos.html", {"lista_platos": lista})

def inicio(req):

    return render(req,"inicio.html", {})

def platos(req):

    return render(req,"platos.html", {})

def clientes(req):

    return render(req,"clientes.html", {})

def Empleados(req):

    return render(req,"empleados.html", {})

def platos_formulario(req):

    print('methos', req.method)
    print('data', req.POST)

    if req.method == 'POST':

        mi_formulario = PlatosFormulario(req.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            nuevo_plato = Plato(nombre = data["plato"], precio = data["precio"])
            nuevo_plato.save()

            return render(req,"inicio.html", {})

        else:
            return render(req,"platos_formulario.html", {"mi_formulario": mi_formulario})

    else:

        mi_formulario = PlatosFormulario()
        return render(req,"platos_formulario.html", {"mi_formulario": mi_formulario})
    

def busqueda_plato(req):
    
    return render(req, "busqueda_plato.html")

def buscar_plato(req):

    nom_plato = req.GET["nombre"]

    plato = Plato.objects.get(nombre = nom_plato)
    

    return render(req,"resultado_busqueda_plato.html", {"plato": plato, "nombre": nom_plato})

