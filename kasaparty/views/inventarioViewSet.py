from rest_framework import viewsets
from kasaparty.models.inventario import Inventario

from kasaparty.serializers.inventarioSerializer import InventarioSerializer


class InventarioViewSet(viewsets.ModelViewSet):
    serializer_class = InventarioSerializer
    queryset = Inventario.objects.all()