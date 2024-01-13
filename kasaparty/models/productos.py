from django.db import models


class Producto(models.Model):
    TIPO_CHOICES = [
        ("DESAYUNO", "Desayuno"),
        ("BOUQUET", "Bouquet de Globos"),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
