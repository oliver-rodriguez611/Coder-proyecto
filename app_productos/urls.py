
from django.urls import path
from .views import *

urlpatterns = [
    path('agrega-plato/<nombre>/<precio>', agrega_plato),
    path('lista_platos/', lista_platos, name= 'platos'),
    path('', inicio, name = 'inicio'),
    path('clientes/', clientes, name = 'clientes'),
    path('empleados/', empleados, name = 'empleados'),
]
