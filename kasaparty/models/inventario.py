from django.db import models

class Inventario(models.Model):
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.TextField()
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_ingreso = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre_producto
