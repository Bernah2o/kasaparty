from django.apps import AppConfig


class KasapartyConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "kasaparty"

    def ready(self):
        from django.contrib import admin
        from kasaparty.models import (
            Cliente,
            Cotizacion,
            Decoracion,
            Evento,
            Inventario,
            Mpago,
            Producto,
            Reserva,
            Componente,
            DetalleProducto,
        )

        admin.site.register(Cliente)
        admin.site.register(Cotizacion)
        admin.site.register(Decoracion)
        admin.site.register(Evento)
        admin.site.register(Inventario)
        admin.site.register(Mpago)
        admin.site.register(Producto)
        admin.site.register(Reserva)
        admin.site.register(Componente)
        admin.site.register(DetalleProducto)
