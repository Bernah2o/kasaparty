from rest_framework import serializers
from kasaparty.models.cotizacion import Cotizacion


class CotizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cotizacion
        fields = [
            "id",
            "cliente",
            "productos",
            "fecha_cotizacion",
            "fecha_evento",
            "validez_dias",
            "total",
        ]
