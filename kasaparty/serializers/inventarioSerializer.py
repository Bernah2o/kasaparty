from rest_framework import serializers
from kasaparty.models.inventario import Inventario

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = "__all__"