from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Perro)
admin.site.register(Sucursal)

admin.site.register(Raza)
admin.site.register(Consulta)
admin.site.register(Vacuna)
admin.site.register(Vacunacion)
admin.site.register(Medicamento)
admin.site.register(Rol)
admin.site.register(HistorialRol)
admin.site.register(DetalleEmpleado)
admin.site.register(Requerimiento)
admin.site.register(EstadoEmpleado)
admin.site.register(Persona)
admin.site.register(HistorialMascotas)
admin.site.register(HistorialEmpleado)
    
