from rest_framework import viewsets

from kasaparty.models.decoracion import Decoracion
from kasaparty.serializers.decoracionSerializer import DecoracionSerializer

class DecoracionViewSet(viewsets.ModelViewSet):
    queryset = Decoracion.objects.all()
    serializer_class = DecoracionSerializer