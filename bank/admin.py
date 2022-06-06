from django.contrib import admin
from .models import BusinessConstant, Client, Card

# Register your models here.
admin.site.register(BusinessConstant)
admin.site.register(Client)
admin.site.register(Card)