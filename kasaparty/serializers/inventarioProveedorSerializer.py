from rest_framework import serializers

from kasaparty.models.inventarioProveedor import InventarioProveedor

class InventarioProeedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventarioProveedor
        fields = "__all__"