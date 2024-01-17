from django.contrib import admin
from django.utils.html import format_html
from django.contrib.humanize.templatetags.humanize import intcomma
from kasaparty.models.inventarioBase import (
    InventarioBase,
    InventarioPropio,
    InventarioProveedor,
)

from .models import (
    Cliente,
    Cotizacion,
    Tematica,
    Evento,
    Mpago,
    Producto,
    Reserva,
    Componente,
    DetalleProducto,
    Proveedor,
)


class ClienteAdmin(admin.ModelAdmin):
    list_display = [
        "numero_documento",
        "nombre",
        "apellido",
        "telefono",
        "fecha_cumpleanos",
        "correo",
    ]


class EventoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "fecha", "cliente", "mostrar_estado"]
    actions = ["marcar_como_terminado"]

    # Hacer el campo estado editable solo si está en "en_curso"
    def get_readonly_fields(self, request, obj=None):
        if obj and obj.estado == "terminado":
            return ["nombre", "fecha", "cliente", "estado"]
        return []

    # Acción personalizada para marcar un evento como "Terminado"
    def marcar_como_terminado(self, request, queryset):
        queryset.update(estado="terminado")

    marcar_como_terminado.short_description = "Marcar como Terminado"

    # Método para mostrar el estado con formato en el panel de administración
    def mostrar_estado(self, obj):
        if obj.estado == "en_curso":
            return format_html('<span style="color:red;">En Curso</span>')
        else:
            return format_html('<span style="color:green;">Terminado</span>')

    mostrar_estado.short_description = "Estado"


class InventarioBaseAdmin(admin.ModelAdmin):
    list_display = [
        "nombre_producto",
        "fecha_ingreso",
        "evento_alquilado",
        "precio",
        "cantidad",
        "asignado"
    ]
    list_filter = ["asignado", "evento_alquilado"]
    search_fields = ["nombre_producto"]

    def precio(self, obj):
        # Utilizamos intcomma para formatear el número con punto de mil
        return intcomma(obj.precio_unitario)

    precio.short_description = "Precio"


class InventarioPropioAdmin(InventarioBaseAdmin):
    list_display = InventarioBaseAdmin.list_display + []

class InventarioProveedorAdmin(InventarioBaseAdmin):
    list_display = InventarioBaseAdmin.list_display + []

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ["nombre", "apellido", "telefono", "nombre_cuenta", "numero_cuenta"]


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Cotizacion)
admin.site.register(Tematica)
admin.site.register(Mpago)
admin.site.register(Producto)
admin.site.register(Reserva)
admin.site.register(Componente)
admin.site.register(DetalleProducto)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(InventarioPropio, InventarioPropioAdmin)
admin.site.register(InventarioProveedor, InventarioProveedorAdmin)
