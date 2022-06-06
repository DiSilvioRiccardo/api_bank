from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import requests

# Create your views here.
def getCardBalanceView(request, card_number):
    if request.method == "GET":
        card = Card.objects.get(card_number = int(card_number))
        return JsonResponse(data={"balance": card.balance})


def getUserBalanceView(request, id_number):
    if request.method == "GET":
        client = Client.objects.get(id = int(id_number))
        cards = Card.objects.filter(owner = client)
        if cards.count() > 0:
            total_balance = sum([card.balance for card in cards])
            return JsonResponse(data={"balance": total_balance})
        else:
            return JsonResponse(data={"balance": 0, "error": "no cards on record"})


def makePaymentView(request):
    if request.method == "POST":
        if request.POST["amount"] <= 0:
            return JsonResponse(data={"result": "negative transaction amount"})
        
        card_number = request.POST['card_number']
        card = Card.objects.get(card_number = int(card_number))
        if request.POST["key"] == card.owner.key and int(request.POST["id_number"]) == card.owner.id:
            if card.balance > int(request.POST["amount"]):
                card.balance -= int(request.POST["amount"])
                card.save()
                if "callback" in request.POST:
                    data = {
                        "result": "done"
                    }

                    if "transaction_number" in request.POST:
                        data["transaction_number"] = request.POST["transaction_number"]

                    requests.post(request.POST["callback"], json=data)
                    print("sent callback")

                return JsonResponse(data={"result": "transaction done"})
            else:
                return JsonResponse(data={"result": "insufficient balance"})
        else:
            return JsonResponse(data={"result": "incorrect key or card not owned by user"})



def showAvailabilityView(request):
    if request.method == "GET":
        data = {}
        for constant in BusinessConstant.objects.all():
            data.update({constant.string_value: constant.boolean_value})
        return JsonResponse(data=data)


