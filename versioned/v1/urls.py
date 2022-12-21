from . import api
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'pago', api.PagoViewSet, 'pagos')

api_urlpatterns = router.urls