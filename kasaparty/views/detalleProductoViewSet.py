from rest_framework import viewsets

from kasaparty.models.detalleProducto import DetalleProducto
from kasaparty.serializers.detalleProductoSerializer import DetalleProductoSerializer

class DetalleProductoViewSet(viewsets.ModelViewSet):
    queryset = DetalleProducto.objects.all()
    serializer_class = DetalleProductoSerializer