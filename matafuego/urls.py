from rest_framework import routers
from .views import (
    MatafuegoModelViewSet,
    TipoMatafuegoModelViewSet,
    ClientesModelViewSet,
    PropiedadModelViewSet,
    TicketModelViewSet,
    ConfiguracionModelViewSet,
    CertificadoModelViewSet
)

router_matafuego = routers.DefaultRouter()

router_matafuego.register('matafuegos',MatafuegoModelViewSet,'matafuegos')
router_matafuego.register('tipoMatafuegos',TipoMatafuegoModelViewSet,'tipoMatafuego')
router_matafuego.register('clientes',ClientesModelViewSet,'clientes')
router_matafuego.register('propiedades',PropiedadModelViewSet,'propiedades')
router_matafuego.register('tickets',TicketModelViewSet,'tickets')
router_matafuego.register('config',ConfiguracionModelViewSet,'config')
router_matafuego.register('certificados',CertificadoModelViewSet,'config')

urlpatterns = router_matafuego.urls
