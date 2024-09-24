from django.shortcuts import render
from django.http import HttpResponse
from .models import Plato

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

def empleados(req):

    return render(req,"empleados.html", {})