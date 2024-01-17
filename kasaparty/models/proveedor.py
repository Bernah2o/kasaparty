from django.db import models


class Proveedor(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ("CEDULA", "Cedula"),
        ("NIT", "NIT"),
    ]
    tipo_documento = models.CharField(max_length=10, choices=TIPO_DOCUMENTO_CHOICES, default= "Cedula")
    numero_documento = models.CharField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, blank=True)
    direccion = models.CharField(max_length=100 , blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    correo = models.EmailField(blank=True)
    nombre_cuenta = models.CharField(max_length=100, blank=True)
    numero_cuenta = models.CharField(max_length=50, blank=True)

    def __str__(self):
        if self.tipo_documento == "NIT":
            return self.nombre
        else:
            return f"{self.nombre} {self.apellido}"
        
    def convertir_campos_a_mayusculas(self):
        self.nombre = self.nombre.upper() if self.nombre else ""
        self.apellido = self.apellido.upper() if self.apellido else ""
        self.direccion = self.direccion.upper() if self.direccion else ""
        self.nombre_cuenta = self.nombre_cuenta.upper() if self.nombre_cuenta else ""

    def save(self, *args, **kwargs):
        self.convertir_campos_a_mayusculas()  # Llamar a la función antes de guardar
        super().save(*args, **kwargs)    
