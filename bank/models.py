from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, default = "John Doe")
    id = models.IntegerField(primary_key=True, auto_created=True, default=1)
    key = models.CharField(max_length = 8, default = "12345678")


class Card(models.Model):
    DEBIT_CARD = 1
    CREDIT_CARD = 2
    
    card_types = (
        (DEBIT_CARD, "Tarjeta de debito"),
        (CREDIT_CARD, "Tarjeta de credito"),
    )

    card_type = models.IntegerField(choices = card_types)
    balance = models.FloatField()
    owner = models.ForeignKey(Client, on_delete=models.PROTECT)
    card_number = models.BigIntegerField()


class BusinessConstant(models.Model):
    PAYMENT_ENDPOINT_ENABLED = 1
    BALANCE_ENDPOINT_ENABLED = 2
    AVAILABILITY_ENDPOINT_ENABLED = 3
    
    BUSINESS_CONSTANTS = (
        (PAYMENT_ENDPOINT_ENABLED, "Endpoint de pago habilitado"),
        (BALANCE_ENDPOINT_ENABLED, "Endpoint de balance habilitado"),
        (AVAILABILITY_ENDPOINT_ENABLED, "Endpoint de disponibilidad habilitado"),
    )

    id = models.IntegerField(primary_key = True, choices = BUSINESS_CONSTANTS)
    boolean_value = models.BooleanField(null = True)
    integer_value = models.IntegerField(null = True)
    string_value = models.CharField(max_length = 50, null = True)

