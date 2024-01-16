from django.db import models

from kasaparty.models.clientes import Cliente
from kasaparty.models.tematicas import Tematica
from django.core.exceptions import ValidationError


class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True)
    tematica = models.ManyToManyField(Tematica)
    inventario = models.ForeignKey("kasaparty.Inventario", on_delete=models.CASCADE)
    inventario_proveedor = models.ForeignKey(
        "kasaparty.InventarioProveedor", on_delete=models.CASCADE
    )
    estado = models.CharField(
        max_length=10,
        choices=[("en_curso", "En Curso"), ("terminado", "Terminado")],
        default="en_curso",
        editable=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.nombre}"

    def convertir_a_mayusculas(self):
        self.nombre = self.nombre.upper()

    def save(self, *args, **kwargs):
        self.convertir_a_mayusculas()  # Llamar a la función antes de guardar
        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        # Verificar si el producto del inventario ya está asignado a otro evento
        if (
            self.inventario
            and self.inventario.asignado
            and self.inventario.evento_alquilado != self
        ):
            raise ValidationError(
                "El producto del inventario ya está asignado a otro evento."
            )

        super().save(*args, **kwargs)
