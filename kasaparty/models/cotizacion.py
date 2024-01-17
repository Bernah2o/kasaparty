from django.db import models

from kasaparty.models.inventarioBase import InventarioPropio, InventarioProveedor
from kasaparty.models.evento import Evento
from kasaparty.models.clientes import Cliente



class Cotizacion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    evento = models.OneToOneField(Evento, on_delete=models.CASCADE)
    inventarios_propios = models.ManyToManyField(InventarioPropio, related_name="cotizaciones_propias+", blank=True)
    inventarios_proveedores = models.ManyToManyField(InventarioProveedor, related_name="cotizaciones_proveedores+", blank=True)
    fecha_cotizacion = models.DateField(auto_now_add=True)
    fecha_evento = models.DateField()
    validez_dias = models.PositiveIntegerField(default=30)
    total = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)

    def obtener_precio_total(self):
        precio_total = 0

        # Calcular el precio total de los inventarios propios
        for inventario_propio in self.inventarios_propios.all():
            precio_total += inventario_propio.precio_unitario

        # Calcular el precio total de los inventarios proveedores
        for inventario_proveedor in self.inventarios_proveedores.all():
            precio_total += inventario_proveedor.precio_unitario

        # Agregar el 70% de la suma de los precios de los inventarios
        precio_total += 0.7 * precio_total

        return precio_total

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Actualizar el total al guardar la cotización
        self.total = self.obtener_precio_total()
        super().save(*args, **kwargs)
    def __str__(self):
        return f"Cotización para {self.cliente} - {self.fecha_cotizacion}"
