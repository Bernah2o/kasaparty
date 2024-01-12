from rest_framework import viewsets
from kasaparty.models.evento import Evento
from kasaparty.serializers.eventoSerializer import EventoSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer