from rest_framework import viewsets
from kasaparty.models.reserva import Reserva
from kasaparty.serializers.reservaSerializer import ReservaSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer