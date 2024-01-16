from rest_framework import serializers
from kasaparty.models.componente import Componente

class ComponenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Componente
        fields = "__all__"
