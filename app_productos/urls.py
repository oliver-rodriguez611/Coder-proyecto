
from django.urls import path
from .views import *

urlpatterns = [
    path('agrega-plato/<nombre>/<precio>', agrega_plato),
    path('lista_platos/', lista_platos, name= 'platos'),
    path('', inicio),
    path('clientes/', clientes),
    path('empleados/', empleados),
]
