from rest_framework import serializers
from kasaparty.models.inventario import Inventario

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = ['id', 'nombre_producto', 'descripcion', 'cantidad', 'precio_unitario', 'fecha_ingreso']