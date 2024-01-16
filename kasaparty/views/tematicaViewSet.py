from rest_framework import viewsets

from kasaparty.models.tematicas import Tematica
from kasaparty.serializers.tematicaSerializer import TematicaSerializer




class TematicaViewSet(viewsets.ModelViewSet):
    queryset = Tematica.objects.all()
    serializer_class = TematicaSerializer