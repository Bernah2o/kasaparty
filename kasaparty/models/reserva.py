from django.db import models

from kasaparty.models import Cliente, Cotizacion, Evento

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    evento = models.OneToOneField(Evento, on_delete=models.CASCADE)
    cotizacion = models.OneToOneField(Cotizacion, on_delete=models.CASCADE)
    fecha_reserva = models.DateField(blank=True)
    anticipo = models.IntegerField(blank=True)
    pendiente = models.IntegerField(blank=True)

    def __str__(self):
        return f"Reserva para {self.evento.nombre}"


@receiver(pre_save, sender=Reserva)
def validar_solapamiento(sender, instance, **kwargs):
    # Verificar que la fecha de la reserva no se solape con ningún evento existente
    eventos_solapados = Evento.objects.filter(
        fecha__range=[instance.fecha_reserva, instance.fecha_reserva],
    ).exclude(id=instance.evento.id)  # Excluye el mismo evento si ya existe
    if eventos_solapados.exists():
        raise ValidationError('La reserva se solapa con otro evento existente.')
