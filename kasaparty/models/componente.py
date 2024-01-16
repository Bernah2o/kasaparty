from django.db import models
from kasaparty.models.productos import Producto


class Componente(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
    def convertir_a_mayusculas(self):
        self.nombre = self.nombre.upper()
