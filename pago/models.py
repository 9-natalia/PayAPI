from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User

# Create your models here.
class Services(models.Model):
    id = models.AutoField(primary_key=True)
    class Servicios(models.TextChoices):
        NETFLIX = 'NF', _('Netflix')
        AMAZON = 'AP', _('Amazon Video')
        START = 'ST', _('Start+')
        PARAMOUNT = 'PM', _('Paramount+')
    name = models.CharField(max_length=2,choices=Servicios.choices,default=Servicios.NETFLIX,)
    description = models.TextField(null=True)
    logo = models.ImageField(null=True)

    class Meta:
        db_table = 'service'

class Pago(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete =models.CASCADE, related_name='users', null=True)
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='service')
    amount = models.FloatField()
    paymentDate = models.DateField(auto_now_add=True)
    expirationDate = models.DateField()

    class Meta:
        db_table = 'pago'

class Expired_pay(models.Model):
    pay_user = models.ForeignKey(Pago, on_delete = models.CASCADE, related_name='pay_user')
    penalty_fee_amount = models.FloatField(default=0.0)

    class Meta:
        db_table = 'pago_caducado'




