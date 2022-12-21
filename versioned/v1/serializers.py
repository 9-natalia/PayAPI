from rest_framework.serializers import ModelSerializer
from pago.models import Pago

class PagoSerializer(ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'
        read_only_fields = '__all__',