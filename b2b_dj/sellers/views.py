from django.shortcuts import render
from users.models import User

# Create your views here.
def main(request):
    return render(request, "sellers/main.html")

def seller_new_offers(request):
    return render(request, "sellers/seller_new_offers.html")

def seller_product(request):
    return render(request, "sellers/seller_product.html")

def seller_order(request):
    return render(request, "sellers/seller_order.html")

def seller_buyers(request):
    buyers = User.objects.all().filter(is_buyer=True)
    return render(request, "sellers/seller_buyers.html",{
        "buyers":buyers,
    })

def seller_carriers(request):
    return render(request, "sellers/seller_carriers.html")

def seller_storage(request):
    return render(request, "sellers/seller_storage.html")