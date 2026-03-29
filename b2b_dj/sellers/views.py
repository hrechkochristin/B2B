from django.shortcuts import render, redirect
from django.db.models import Prefetch
from users.models import User
from products.models import Product
from orders.models import Order
from carts.models import CartItem

# Create your views here.
def main(request):
    return render(request, "sellers/main.html")

def seller_new_offers(request):
    username = request.session.get("username")

    if not username:
        return redirect("main")

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect("main")

    orders = (
        Order.objects
        .filter(seller=user, status="created")
        .select_related("buyer", "delivery")
        .prefetch_related(
            Prefetch("items", queryset=CartItem.objects.select_related("product"))
        )
        .order_by("-created_at")
    )

    return render(request, "sellers/seller_new_offers.html", {
        "orders": orders,
    })

def seller_product(request):
    username = request.session.get("username")

    if not username:
        return redirect("main")

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect("main")

    if request.method == "POST":
        features = request.POST.getlist("features")
        temp_ranges = request.POST.getlist("temp_range")

        Product.objects.create(
            seller=user,
            name=request.POST.get("productName"),
            category=request.POST.get("productCategory") or "other",
            price=request.POST.get("productPrice") or 0,
            origin_location=request.POST.get("originLocation") or "Не вказано",
            origin_storage=request.POST.get("originStorage") or "",
            quantity=request.POST.get("productStock") or 0,
            stock="in_stock",
            weight=request.POST.get("productWeight") or 0,
            volume=request.POST.get("productVolume") or 0,
            is_perishable="perishable" in features,
            is_fragile="fragile" in features,
            is_animal_origin="animal_origin" in features,
            is_hazardous="hazardous" in features,
            temperature_regime=temp_ranges[0] if temp_ranges else "no_control",
            description=request.POST.get("productDescription") or ""
        )

        return redirect("seller_product")

    products = Product.objects.filter(seller=user).order_by("-id")

    return render(request, "sellers/seller_product.html", {
        "products": products,
    })

def seller_order(request):
    username = request.session.get("username")

    if not username:
        return redirect("main")

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect("main")

    orders = (
        Order.objects
        .filter(seller=user)
        .select_related("buyer", "delivery")
        .prefetch_related(
            Prefetch("items", queryset=CartItem.objects.select_related("product")),
            "products"
        )
        .order_by("-id")
    )

    return render(request, "sellers/seller_order.html", {
        "orders": orders,
    })

def seller_buyers(request):
    buyers = User.objects.all().filter(is_buyer=True)
    return render(request, "sellers/seller_buyers.html",{
        "buyers":buyers,
    })

def seller_carriers(request):
    return render(request, "sellers/seller_carriers.html")

def seller_storage(request):
    return render(request, "sellers/seller_storage.html")