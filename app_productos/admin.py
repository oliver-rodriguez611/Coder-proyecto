from django.contrib import admin
from .models import Plato, clientes, empleados
# Register your models here.

admin.site.register(Plato)
admin.site.register(clientes)
admin.site.register(empleados)