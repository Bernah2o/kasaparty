from django.db import models


class Cliente(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ("CEDULA", "Cedula"),
        ("NIT", "NIT"),
    ]
    tipo_documento = models.CharField(max_length=10, choices=TIPO_DOCUMENTO_CHOICES, default="Cedula")
    numero_documento = models.CharField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, blank=True)
    direccion = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    fecha_cumpleanos = models.DateField(blank=True)
    correo = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def convertir_a_mayusculas(self):
        self.nombre = self.nombre.upper()
        self.apellido = self.apellido.upper()
        self.direccion = self.direccion.upper()
