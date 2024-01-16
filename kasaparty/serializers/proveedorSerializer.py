from rest_framework import serializers

from kasaparty.models.proveedor import Proveedor

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ['id', 'nombre', 'direccion', 'telefono', 'correo', 'productos_suministrados','numero_cuenta','nombre_cuenta ']