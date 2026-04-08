from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from orders.models import Order
from users.models import User
from products.models import Product
from carts.models import CartItem
from orders.models import Order

def main(request):
    return render(request, "carriers/main.html")

def carrier_sellers(request):
    return render(request, "carriers/carrier_sellers.html")

def carrier_deliveries(request):
    return render(request, "carriers/carrier_deliveries.html")

def carrier_orders(request):
    return render(request, "carriers/carrier_orders.html")

def carrier_transport(request):
    return render(request, "carriers/carrier_transport.html")