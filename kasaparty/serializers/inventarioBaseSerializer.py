from rest_framework import serializers
from kasaparty.models.inventarioBase import InventarioBase

class InventarioBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventarioBase
        fields = "__all__"