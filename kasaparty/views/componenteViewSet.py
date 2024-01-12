from rest_framework import viewsets
from kasaparty.models.componente import Componente
from kasaparty.serializers.componenteSerializer import ComponenteSerializer

class ComponenteViewSet(viewsets.ModelViewSet):
    queryset = Componente.objects.all()
    serializer_class = ComponenteSerializer