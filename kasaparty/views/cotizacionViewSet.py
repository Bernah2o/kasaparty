from rest_framework import viewsets
from kasaparty.models.cotizacion import Cotizacion
from kasaparty.serializers.cotizacionSerializer import CotizacionSerializer

class CotizacionViewSet(viewsets.ModelViewSet):
    queryset = Cotizacion.objects.all()
    serializer_class = CotizacionSerializer