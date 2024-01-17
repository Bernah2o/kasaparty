from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from kasaparty.views.clienteViewSet import ClienteViewSet
from kasaparty.views.componenteViewSet import ComponenteViewSet
from kasaparty.views.cotizacionViewSet import CotizacionViewSet
from kasaparty.views.tematicaViewSet import TematicaViewSet
from kasaparty.views.detalleProductoViewSet import DetalleProductoViewSet
from kasaparty.views.eventoViewSet import EventoViewSet
from kasaparty.views.inventarioBaseViewSet import InventarioBaseViewSet
from kasaparty.views.mpagoViewSet import MpagoViewSet
from kasaparty.views.productosViewSet import ProductosViewSet
from kasaparty.views.proveedorViewSet import ProveedorViewSet
from kasaparty.views.reservaViewSet import ReservaViewSet



router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'componente', ComponenteViewSet)
router.register(r'cotizacion', CotizacionViewSet)
router.register(r'tematica', TematicaViewSet)
router.register(r'detalleProducto', DetalleProductoViewSet)
router.register(r'evento', EventoViewSet)
router.register(r'inventario', InventarioBaseViewSet, basename='inventario-base')
router.register(r'mpago', MpagoViewSet)
router.register(r'productos', ProductosViewSet)
router.register(r'reserva', ReservaViewSet)
router.register(r'proveedor', ProveedorViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
]
