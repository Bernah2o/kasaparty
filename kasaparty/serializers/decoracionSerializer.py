from rest_framework import serializers
from kasaparty.models.decoracion import Decoracion


class DecoracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decoracion
        fields = ['id', 'nombre', 'descripcion', 'precio']