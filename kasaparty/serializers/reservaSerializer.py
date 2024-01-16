from rest_framework import serializers

from kasaparty.models.reserva import Reserva

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = "__all__"