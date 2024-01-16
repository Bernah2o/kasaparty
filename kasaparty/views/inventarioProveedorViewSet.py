from rest_framework import viewsets

from kasaparty.models.inventarioProveedor import InventarioProveedor
from kasaparty.serializers import inventarioProveedorSerializer

class InventarioProveedorViewSet(viewsets.ModelViewSet):
    queryset = InventarioProveedor.objects.all()
    serializer_class = inventarioProveedorSerializer
