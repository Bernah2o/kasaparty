from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from kasaparty.models.evento import Evento


class Inventario(models.Model):
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
        self.convertir_a_mayusculas()  # Llamar a la función antes de guardar
        super().save(*args, **kwargs)


def liberar_inventario(sender, instance, **kwargs):
    if instance.estado == 'terminado':
        # Evento terminado, liberar productos en el inventario
        productos_asignados = Inventario.objects.filter(evento_alquilado=instance)
        for producto in productos_asignados:
            producto.asignado = False
            producto.evento_alquilado = None
            producto.save()

@receiver(post_delete, sender=Evento)
def liberar_inventario_al_eliminar(sender, instance, **kwargs):
    # Si se elimina un evento, liberar los productos asignados a ese evento
    productos_asignados = Inventario.objects.filter(evento_alquilado=instance)
    for producto in productos_asignados:
        producto.asignado = False
        producto.evento_alquilado = None
        producto.save()
    