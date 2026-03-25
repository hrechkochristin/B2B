from django.shortcuts import render

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
    return render(request, "sellers/seller_buyers.html")

def seller_carriers(request):
    return render(request, "sellers/seller_carriers.html")

def seller_storage(request):
    return render(request, "sellers/seller_storage.html")