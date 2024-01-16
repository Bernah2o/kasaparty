from django.db import models
from kasaparty.models.proveedor import Proveedor


class InventarioProveedor(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.TextField()
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.IntegerField()
    fecha_ingreso = models.DateField(auto_now_add=True)
    disponible = models.CharField(max_length=2, choices=[("SI", "SI"), ("NO", "NO")], default="SI", editable=False)
    evento_alquilado = models.ForeignKey(
        "kasaparty.Evento",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="inventario_proveedor_evento_alquilado",
        editable=False,
    )
    asignado = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return f"{self.proveedor} - {self.nombre_producto}"

    def convertir_a_mayusculas(self):
        self.nombre_producto = self.nombre_producto.upper()

    def save(self, *args, **kwargs):
        self.convertir_a_mayusculas()  # Llamar a la función antes de guardar
        super().save(*args, **kwargs)

    def marcar_como_alquilado(self, evento):
        self.disponible = False
        self.evento_alquilado = evento if evento else None
        self.asignado = True
        self.save()

    def liberar_alquiler(self):
        self.disponible = True
        self.evento_alquilado = None
        self.asignado = False
        self.save()
