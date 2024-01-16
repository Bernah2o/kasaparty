from rest_framework import serializers
from kasaparty.models.cotizacion import Cotizacion


class CotizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cotizacion
        fields = "__all__"
