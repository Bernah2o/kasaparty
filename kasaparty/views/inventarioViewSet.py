from rest_framework import viewsets
from kasaparty.models.inventario import Inventario

from kasaparty.serializers.inventarioSerializer import InventarioSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer