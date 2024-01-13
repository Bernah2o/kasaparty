from django.db import models

from kasaparty.models.clientes import Cliente
from kasaparty.models.productos import Producto


class Cotizacion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    fecha_cotizacion = models.DateField(auto_now_add=True)
    fecha_evento = models.DateField()
    validez_dias = models.PositiveIntegerField(default=7)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Cotización para {self.cliente} - {self.fecha_cotizacion}"
