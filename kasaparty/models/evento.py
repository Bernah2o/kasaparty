from django.db import models
from kasaparty.models.clientes import Cliente
from kasaparty.models.decoracion import Decoracion

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    descripcion = models.TextField()
    decoraciones = models.ManyToManyField(Decoracion)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
    def convertir_a_mayusculas(self):
        self.nombre = self.nombre.upper()
