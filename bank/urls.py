from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    #consultar saldo tarjeta
    re_path(r"^balance/(?P<card_number>\w{16})$", views.getCardBalanceView),
    #consultar saldo usuario
    re_path(r"^balance/(?P<id_number>\w{8,10})$", views.getUserBalanceView),
    #realizar pago
    path("pay", views.makePaymentView),
    #mostrar disponibilidad de endpoints
    path("availability", views.showAvailabilityView),
]