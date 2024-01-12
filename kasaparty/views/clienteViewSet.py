from rest_framework import viewsets
from kasaparty.models.clientes import Cliente
from kasaparty.serializers.clienteSerializer import ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer