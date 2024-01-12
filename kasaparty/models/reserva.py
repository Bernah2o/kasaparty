from django.db import models
from kasaparty.models.evento import Evento


class Reserva(models.Model):
    evento = models.OneToOneField(Evento, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Reserva para {self.evento.nombre}"
