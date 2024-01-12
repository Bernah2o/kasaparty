from rest_framework import serializers

from kasaparty.models.productos import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'tipo', 'precio']