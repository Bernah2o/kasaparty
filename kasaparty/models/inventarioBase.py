from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


class InventarioBase(models.Model):
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.TextField()
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.IntegerField()
    fecha_ingreso = models.DateField(auto_now_add=True)
    evento_alquilado = models.ForeignKey(
        "kasaparty.Evento",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="inventario_evento_alquilado",
        editable=False,
    )
    asignado = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return self.nombre_producto

    def convertir_a_mayusculas(self):
        self.nombre_producto = self.nombre_producto.upper()

    def save(self, *args, **kwargs):
        self.convertir_a_mayusculas()

        # Verificar si el inventario ya está asignado a otro evento
        if self.asignado and self.evento_alquilado != self.evento_alquilado_anterior:
            raise ValueError("El inventario ya está asignado a otro evento")
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class InventarioPropio(InventarioBase):
    evento_alquilado_anterior = models.ForeignKey(
        "kasaparty.Evento",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
        editable=False,
    )
    evento_alquilado = models.ForeignKey(
        "kasaparty.Evento",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="inventario_propio_rel",
        editable=False,
    )


class InventarioProveedor(InventarioBase):
    evento_alquilado_anterior = models.ForeignKey(
        "kasaparty.Evento",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
        editable=False,
    )
    evento_alquilado = models.ForeignKey(
        "kasaparty.Evento",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="inventario_proveedor_rel",
        editable=False,
    )


@receiver(post_delete, sender="kasaparty.Evento")
def liberar_inventario(sender, instance, **kwargs):
    if instance.estado == "terminado":
        InventarioPropio.objects.filter(evento_alquilado=instance).update(
            asignado=False, evento_alquilado=None
        )

        InventarioProveedor.objects.filter(evento_alquilado=instance).update(
            asignado=False, evento_alquilado=None
        )
