
from rest_framework import viewsets
from kasaparty.models.mpago import Mpago
from kasaparty.serializers.mpagoSerializer import MpagoSerializer


class MpagoViewSet(viewsets.ModelViewSet):
    queryset = Mpago.objects.all()
    serializer_class = MpagoSerializer