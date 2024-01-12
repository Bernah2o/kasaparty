from rest_framework import serializers
from kasaparty.models.detalleProducto import DetalleProducto

class DetalleProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleProducto
        fields = ['id', 'producto', 'nombre', 'descripcion', 'precio']