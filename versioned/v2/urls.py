from rest_framework import routers
from . import api

router = routers.DefaultRouter()
router.register(r'pagos', api.PagoViewSet, 'pagos')
router.register(r'servicios', api.ServicesViewSet, 'servicios')

urlpatterns = router.urls