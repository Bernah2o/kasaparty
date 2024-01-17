from django.db import models

from kasaparty.models.clientes import Cliente
from django.db.models.signals import post_save
from django.dispatch import receiver


class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True)
    tematica = models.ForeignKey(
        "kasaparty.Tematica", on_delete=models.SET_NULL, null=True, blank=True
    )
    inventario_propio = models.OneToOneField(
        "kasaparty.InventarioPropio",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="evento_inventario_propio",
    )
    inventario_proveedor = models.OneToOneField(
        "kasaparty.InventarioProveedor",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="evento_inventario_proveedor",
    )
    estado = models.CharField(
        max_length=10,
        choices=[("en_curso", "En Curso"), ("terminado", "Terminado")],
        default="en_curso",
        editable=False,
        blank=True,
    )

    def __str__(self):
        return f"{self.nombre}"

    def convertir_a_mayusculas(self):
        self.nombre = self.nombre.upper()

    def save(self, *args, **kwargs):
        # Guardar primero el objeto Evento
        super().save(*args, **kwargs)
        self.convertir_a_mayusculas()

        # Verificar si el evento está terminado antes de asignar inventarios
        if self.estado != "terminado":
            if self.inventario_propio:
                self.inventario_propio.evento_alquilado = self
                self.inventario_propio.save()

            if self.inventario_proveedor:
                self.inventario_proveedor.evento_alquilado = self
                self.inventario_proveedor.save()

        if self.tematica:
            self.tematica.evento = self
            self.tematica.save()

    class Meta:
        verbose_name_plural = "Eventos"
