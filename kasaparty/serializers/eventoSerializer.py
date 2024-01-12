from rest_framework import serializers

from kasaparty.models.evento import Evento

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['id', 'fecha', 'descripcion', 'decoraciones', 'cliente']