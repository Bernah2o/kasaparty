from django.apps import AppConfig

from kasaparty.admin import ClienteAdmin, EventoAdmin, InventarioAdmin, InventarioProveedorAdmin, ProveedorAdmin


class KasapartyConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "kasaparty"

    def ready(self):
        import kasaparty.models.signals # Si tienes señales en tu aplicación
        from django.contrib import admin
        from kasaparty.models import (
            Cliente,
            Cotizacion,
            Tematica,
            Evento,
            Inventario,
            Mpago,
            Producto,
            Reserva,
            Componente,
            DetalleProducto,
            Proveedor,
            InventarioProveedor,
        )

        admin.site.register(Cliente, ClienteAdmin)
        admin.site.register(Cotizacion)
        admin.site.register(Tematica)
        admin.site.register(Inventario, InventarioAdmin)
        admin.site.register(Mpago)
        admin.site.register(Producto)
        admin.site.register(Reserva)
        admin.site.register(Componente)
        admin.site.register(DetalleProducto)
        admin.site.register(Proveedor, ProveedorAdmin)
        admin.site.register(Evento, EventoAdmin)
        admin.site.register(InventarioProveedor, InventarioProveedorAdmin)