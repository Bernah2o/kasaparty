from django.db import models
from kasaparty.models.componente import Componente
from kasaparty.models.productos import Producto


class DetalleProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad} {self.componente.nombre} para {self.producto.nombre}"
