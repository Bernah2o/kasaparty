from rest_framework import viewsets

from kasaparty.models.proveedor import Proveedor
from kasaparty.serializers.proveedorSerializer import ProveedorSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer