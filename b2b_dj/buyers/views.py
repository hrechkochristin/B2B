from django.shortcuts import render
from users.models import User

# Create your views here.
def main(request):
    return render(request, "buyers/main.html")

def buyer_catalog(request):
    return render(request, "buyers/buyer_catalog.html")

def buyer_orders(request):
    return render(request, "buyers/buyer_orders.html")

def buyer_process(request):
    return render(request, "buyers/buyer_process.html")

def buyer_sellers(request):
    sellers = User.objects.all().filter(is_seller=True)
    return render(request, "buyers/buyer_sellers.html",{
        "sellers":sellers,
    })