from .models import Pago, Services
from rest_framework import viewsets
from .serializers import PagoSerializer, ServicesSerializer
from rest_framework.permissions import IsAuthenticated
from .pagination import StandardResultsSetPagination
from rest_framework import viewsets, filters 

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.get_queryset().order_by('id')
    serializer_class = PagoSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]

    search_fields = ['usuario__id', 'fecha_pago', 'servicio']
    throttle_scope = 'pagos'

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.get_queryset().order_by('id')
    serializer_class = ServicesSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]
    
    search_fields = ['id', 'name', 'description', 'logo']