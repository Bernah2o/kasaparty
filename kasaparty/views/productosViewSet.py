from rest_framework import viewsets
from kasaparty.models.productos import Producto
from kasaparty.serializers.productosSerializer import ProductoSerializer

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer