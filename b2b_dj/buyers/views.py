from django.shortcuts import render

from orders.models import Order
from users.models import User
from products.models import Product

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

def buyer_catalog(request):
    products = Product.objects.all()
    return render(request, "buyers/buyer_catalog.html",{
        "products":products,
    })

def buyer_orders(request):
    # Вибираємо тільки замовлення поточного користувача
    orders = Order.objects.filter(user=request.user).prefetch_related('items__product')

    return render(request, "buyers/buyer_orders.html", {
        "orders": orders,
    })