from django.contrib import admin
from django.contrib.admin.models import LogEntry

from .models import CargoEmpleado,Cliente,Comuna,Departamento,Empleado,EstadoDepartamento,EstadoInmueble,EstadoReserva,FacturaBoleta,Inventario,MantencionDepartamento,Nacion,Region,ReservaDepartamento,ServiciosBasicos,ServiciosExtra,ZonaMueble

# Register your models here.
admin.site.register(CargoEmpleado)
admin.site.register(Cliente)
admin.site.register(Comuna)
admin.site.register(Departamento)
admin.site.register(Empleado)
admin.site.register(EstadoDepartamento)
admin.site.register(EstadoInmueble)
admin.site.register(EstadoReserva)
admin.site.register(FacturaBoleta)
admin.site.register(Inventario)
admin.site.register(MantencionDepartamento)
admin.site.register(Nacion)
admin.site.register(Region)
admin.site.register(ReservaDepartamento)
admin.site.register(ServiciosBasicos)
admin.site.register(ServiciosExtra)
admin.site.register(ZonaMueble)


# Linea siguiente n°27 sirve para eliminar las ultimas acciones de admin
# LogEntry.objects.all().delete()