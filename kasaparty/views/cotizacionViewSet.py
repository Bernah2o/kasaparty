from rest_framework import viewsets

from kasaparty.models import Cliente, Evento
from kasaparty.models.cotizacion import Cotizacion
from kasaparty.models.inventarioBase import InventarioPropio, InventarioProveedor
from kasaparty.serializers.cotizacionSerializer import CotizacionSerializer

from rest_framework.response import Response

class CotizacionViewSet(viewsets.ModelViewSet):
    queryset = Cotizacion.objects.all()
    serializer_class = CotizacionSerializer

    def create(self, request, *args, **kwargs):
        # Asegúrate de tener los datos necesarios en la solicitud (puedes ajustar esto según tus necesidades)
        cliente_id = request.data.get('cliente')
        evento_id = request.data.get('evento')
        fecha_evento = request.data.get('fecha_evento')
        # ... otras propiedades

        # Obtén o crea instancias de Cliente, Evento, etc.
        cliente = Cliente.objects.get(pk=cliente_id)
        evento = Evento.objects.get(pk=evento_id)
        # ... otras instancias

        # Crea la cotización
        cotizacion = Cotizacion.objects.create(cliente=cliente, evento=evento, fecha_evento=fecha_evento)

        # Añade inventarios propios y proveedores según tus necesidades
        inventarios_propios_ids = request.data.getlist('inventarios_propios', [])
        inventarios_proveedores_ids = request.data.getlist('inventarios_proveedores', [])

        for inventario_propio_id in inventarios_propios_ids:
            inventario_propio = InventarioPropio.objects.get(pk=inventario_propio_id)
            cotizacion.inventarios_propios.add(inventario_propio)

        for inventario_proveedor_id in inventarios_proveedores_ids:
            inventario_proveedor = InventarioProveedor.objects.get(pk=inventario_proveedor_id)
            cotizacion.inventarios_proveedores.add(inventario_proveedor)

        serializer = CotizacionSerializer(cotizacion)
        return Response(serializer.data)