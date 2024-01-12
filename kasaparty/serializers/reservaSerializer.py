from rest_framework import serializers

from kasaparty.models.reserva import Reserva

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id', 'evento', 'fecha_reserva', 'monto_total']