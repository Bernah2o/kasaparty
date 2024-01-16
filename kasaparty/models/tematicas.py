from django.db import models
class Tematica(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

    def convertir_a_mayusculas(self):
        self.nombre = self.nombre.upper()
        
    def save(self, *args, **kwargs):
        self.convertir_a_mayusculas()  # Llamar a la función antes de guardar
        super().save(*args, **kwargs)    