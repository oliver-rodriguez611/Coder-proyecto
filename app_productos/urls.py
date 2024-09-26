
from django.urls import path
from .views import *

urlpatterns = [
    path('agrega-plato/<nombre>/<precio>', agrega_plato),
    path('lista_platos/', lista_platos, name= 'platos'),
    path('', inicio, name = 'inicio'),
    path('clientes/', Clientes, name = 'clientes'),
    path('empleados/', Empleados, name = 'empleados'),
    path('platos_formulario/', platos_formulario, name = 'platos_formulario'),
    path('clientes_formulario/', clientes_formulario, name = 'clientes_formulario'),
    path('empleados_formulario/', empleados_formulario, name = 'empleados_formulario'),
    path('busqueda_plato/', busqueda_plato, name = 'BusquedaPlato'),
    path('buscar_plato/', buscar_plato, name = 'BuscarPlato'),
]
