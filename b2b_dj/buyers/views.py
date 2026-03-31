from django.shortcuts import render, redirect
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
        try:
            quantity = int(request.POST.get("quantity", 1))
            price = float(request.POST.get("price", 0))
        except (ValueError, TypeError):
            quantity = 1
            price = 0

        if product_id:
            # ВИПРАВЛЕННЯ ПОМИЛКИ MultipleObjectsReturned:
            # Шукаємо всі існуючі записи цього товару в кошику користувача
            items = CartItem.objects.filter(buyer=user, product_id=product_id)
            
            if items.exists():
                # Якщо є хоча б один — беремо перший і оновлюємо кількість
                cart_item = items.first()
                cart_item.quantity += quantity
                cart_item.save()
            else:
                # Якщо немає — створюємо новий
                CartItem.objects.create(
                    buyer=user,
                    product_id=product_id,
                    quantity=quantity,
                    price=price
                )

            new_count = CartItem.objects.filter(buyer=user).count()

            # Повертаємо це число в JavaScript
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    "success": True, 
                    "new_count": new_count  # Це значення JS підставить у .cart-count
                })

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

def buyer_process(request):
    return render(request, "buyers/buyer_process.html")

def buyer_sellers(request):
    sellers = User.objects.filter(is_seller=True)
    return render(request, "buyers/buyer_sellers.html", {"sellers": sellers})

def cart_view(request):
    username = request.session.get("username")
    if not username: return redirect("main")
    user = User.objects.get(username=username)
    
    cart_items = CartItem.objects.filter(buyer=user).select_related("product")
    return render(request, 'buyers/buyer_cart.html', {"cart_items": cart_items})
