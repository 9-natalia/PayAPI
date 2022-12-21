from rest_framework.serializers import ModelSerializer
from pago.models import Pago, Services, Expired_pay

class PagoSerializer(ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'
        read_only_fields = '__all__',

class ServicesSerializer(ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'
        read_only_fields = '__all__',

class ExpiredSerializer(ModelSerializer):
    class Meta:
        model = Expired_pay
        fields = '__all__'
        read_only_fields = '__all__',
