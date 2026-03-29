import os
import django
import random
from faker import Faker
from decimal import Decimal
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'b2b_dj.settings')
django.setup()

from users.models import User
from orders.models import Order
from products.models import Product
from deliveries.models import Delivery
from carts.models import CartItem  # Переконайся, що шлях до моделі правильний

fake = Faker()

# 1. СТВОРЕННЯ КОРИСТУВАЧІВ
User.objects.all().delete() # Очистка перед заповненням
users = []
for _ in range(10):
    user = User.objects.create(
        username=fake.user_name(),
        email=fake.email(),
        name=fake.first_name(),
        surname=fake.last_name(),
        is_seller=random.choice([True, False]),
        is_buyer=random.choice([True, False]),
        is_carrier=random.choice([True, False]),
    )
    user.set_password("password123")
    user.save()
    users.append(user)

sellers = [u for u in users if u.is_seller] or users
buyers = [u for u in users if u.is_buyer] or users
carriers = [u for u in users if u.is_carrier] or users
print("✅ Users created")

# 2. СТВОРЕННЯ ТОВАРІВ
Product.objects.all().delete()
products = []
for _ in range(15):
    product = Product.objects.create(
        seller=random.choice(sellers),
        name=fake.word().capitalize(),
        category=random.choice([c[0] for c in Product.CATEGORY_CHOICES]),
        price=Decimal(random.randint(50, 2000)),
        origin_location=fake.city(),
        quantity=random.randint(10, 100),
        weight=round(random.uniform(0.1, 10.0), 2),
        volume=round(random.uniform(0.01, 0.5), 2),
        temperature_regime=random.choice([c[0] for c in Product.TEMPERATURE_CHOICES]),
    )
    products.append(product)
print("✅ Products created")

# 3. СТВОРЕННЯ ДОСТАВОК
Delivery.objects.all().delete()
deliveries = []
for _ in range(5):
    delivery = Delivery.objects.create(
        carrier=random.choice(carriers),
        vehicle_info=f"{fake.company()} Truck",
        start_location=fake.city(),
        end_location=fake.city(),
        status=random.choice(['planned', 'in_progress', 'completed']),
    )
    deliveries.append(delivery)
print("✅ Deliveries created")

# 4. СТВОРЕННЯ ЗАМОВЛЕНЬ ТА КАРТ-АЙТЕМІВ
Order.objects.all().delete()
CartItem.objects.all().delete()

for _ in range(12):
    current_buyer = random.choice(buyers)
    
    # Вирішуємо: це буде активний кошик чи вже замовлення?
    is_ordered = random.choice([True, True, False]) # 2/3 шансу, що це замовлення

    if is_ordered:
        # Створюємо Order (Заголовок)
        order = Order.objects.create(
            seller=random.choice(sellers),
            buyer=current_buyer,
            pickup_address=fake.address(),
            delivery_address=fake.address(),
            delivery=random.choice(deliveries),
            status=random.choice(['created', 'confirmed', 'delivered']),
            time_started=timezone.now() if random.random() > 0.5 else None,
            notes=fake.sentence()
        )
        
        # Створюємо CartItem, прив'язаний до замовлення
        selected_products = random.sample(products, random.randint(1, 4))
        for prod in selected_products:
            CartItem.objects.create(
                buyer=current_buyer,
                order=order, # ПРИВ'ЯЗКА ТУТ
                product=prod,
                quantity=random.randint(1, 5),
                price=prod.price # Фіксуємо ціну
            )
    else:
        # Створюємо просто товар у кошику (без Order)
        CartItem.objects.create(
            buyer=current_buyer,
            order=None, # ЗАМОВЛЕННЯ НЕМАЄ
            product=random.choice(products),
            quantity=random.randint(1, 3),
            price=random.choice(products).price
        )

print("✅ Data generated: Orders and CartItems (both in-cart and in-order)")
print("🎉 SUCCESS: База заповнена за твоєю схемою (CartItem замість OrderItem)")