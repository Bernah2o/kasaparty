from rest_framework import serializers
from kasaparty.models.clientes import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'apellido', 'telefono', 'direccion', 'tipo_documento', 'fecha_cumpleanos', 'correo']
