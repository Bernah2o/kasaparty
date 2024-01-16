from rest_framework import serializers
from kasaparty.models.clientes import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"
