from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from users.models import User
from products.models import Product
from carts.models import CartItem
from orders.models import Order

def main(request):
    return render(request, "buyers/main.html")

def buyer_catalog(request):
    # 1. Перевірка користувача
    username = request.session.get("username")
    if not username:
        return redirect("main")

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect("main")

    # 2. Обробка додавання товару (POST)
    if request.method == "POST":
        product_id = request.POST.get("productId")
        quantity = int(request.POST.get("quantity", 1))

        if product_id:
            try:
                product = Product.objects.get(id=product_id)
                # Беремо ціну з товару в базі, а не з POST (так безпечніше)
                product_price = product.price 

                # Використовуємо get_or_create для чистоти коду
                cart_item, created = CartItem.objects.get_or_create(
                    buyer=user,
                    product=product,
                    defaults={'quantity': quantity, 'price': product_price}
                )

                if not created:
                    cart_item.quantity += quantity
                    cart_item.save()

                # Рахуємо загальну кількість УНІКАЛЬНИХ позицій у кошику
                new_count = CartItem.objects.filter(buyer=user).count()

                # ПОВЕРТАЄМО ВІДПОВІДЬ ЗАВЖДИ ДЛЯ POST
                return JsonResponse({
                    "success": True, 
                    "new_count": new_count
                })

            except Product.DoesNotExist:
                return JsonResponse({"success": False, "error": "Товар не знайдено"}, status=404)
            except Exception as e:
                return JsonResponse({"success": False, "error": str(e)}, status=500)

    # 3. Відображення сторінки (GET)
    products = Product.objects.all()
    carts = CartItem.objects.filter(buyer=user).select_related("product")

    return render(request, "buyers/buyer_catalog.html", {
        "carts": carts,
        "products": products
    })

def buyer_orders(request):
    username = request.session.get("username")
    if not username: return redirect("main")
    
    user = User.objects.get(username=username)
    orders = Order.objects.filter(buyer=user).prefetch_related('items__product')
    return render(request, "buyers/buyer_orders.html", {"orders": orders})


def buyer_sellers(request):
    sellers = User.objects.filter(is_seller=True)
    return render(request, "buyers/buyer_sellers.html", {"sellers": sellers})

def cart_view(request):
    username = request.session.get("username")
    if not username: return redirect("main")
    user = User.objects.get(username=username)
    
    cart_items = CartItem.objects.filter(buyer=user).select_related("product")
    return render(request, 'buyers/buyer_cart.html', {"cart_items": cart_items})


def add_to_cart(request):
    if request.method != "POST":
        return redirect("buyer_catalog")

    username = request.session.get("username")
    if not username:
        return redirect("main")

    try:
        buyer = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect("main")

    product_id = request.POST.get("product_id")
    quantity = int(request.POST.get("quantity", 1))

    product = get_object_or_404(Product, id=product_id)

    cart_item, created = CartItem.objects.get_or_create(
        buyer=buyer,
        product=product,
        order=None,
        defaults={
            "quantity": quantity,
            "price": product.price,
        }
    )

    if not created:
        cart_item.quantity += quantity
        cart_item.save()

    return redirect("buyer_catalog")