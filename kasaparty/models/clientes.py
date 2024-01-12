from django.db import models


class Cliente(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ("CEDULA", "Cédula"),
        ("NIT", "NIT"),
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()
    tipo_documento = models.CharField(max_length=10, choices=TIPO_DOCUMENTO_CHOICES)
    fecha_cumpleanos = models.DateField()
    correo = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def convertir_a_mayusculas(self):
        self.nombre = self.nombre.upper()
        self.apellido = self.apellido.upper()
        self.direccion = self.direccion.upper()
        self.correo = self.correo.upper()
