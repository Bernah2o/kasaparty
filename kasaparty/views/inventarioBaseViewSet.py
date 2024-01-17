from rest_framework import viewsets
from kasaparty.models.inventarioBase import InventarioPropio, InventarioProveedor
from kasaparty.serializers.inventarioBaseSerializer import InventarioBaseSerializer


class InventarioBaseViewSet(viewsets.ModelViewSet):
    serializer_class = InventarioBaseSerializer
    
    def get_queryset(self):
        inventario_propio = InventarioPropio.objects.all()
        inventario_proveedor = InventarioProveedor.objects.all()

        # Combina los resultados de ambas consultas
        queryset = list(inventario_propio) + list(inventario_proveedor)

        return queryset
