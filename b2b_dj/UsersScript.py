import os
import django
import random
from faker import Faker
from decimal import Decimal
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'b2b_dj.settings')
django.setup()

from users.models import User
from orders.models import Order, OrderItem
from products.models import Product
from deliveries.models import Delivery

fake = Faker()

# -----------------------
# 1. USERS
# -----------------------

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

print("✅ Users created")

sellers = [u for u in users if u.is_seller] or users
buyers = [u for u in users if u.is_buyer] or users
carriers = [u for u in users if u.is_carrier] or users

# -----------------------
# 2. PRODUCTS
# -----------------------

products = []

for _ in range(10):
    product = Product.objects.create(
        seller=random.choice(sellers),
        name=fake.word(),

        category=random.choice([c[0] for c in Product.CATEGORY_CHOICES]),
        price=Decimal(random.randint(10, 500)),

        origin_location=fake.city(),
        origin_storage=fake.company(),

        quantity=random.randint(1, 50),
        stock=random.choice([c[0] for c in Product.STOCK_CHOISES]),

        weight=round(random.uniform(0.5, 20), 2),
        volume=round(random.uniform(0.01, 2), 2),

        is_perishable=random.choice([True, False]),
        is_fragile=random.choice([True, False]),
        is_animal_origin=random.choice([True, False]),
        is_hazardous=random.choice([True, False]),

        temperature_regime=random.choice([c[0] for c in Product.TEMPERATURE_CHOICES]),

        description=fake.text(max_nb_chars=100),
    )
    products.append(product)

print("✅ Products created")

# -----------------------
# 3. DELIVERIES
# -----------------------

deliveries = []

for _ in range(10):
    delivery = Delivery.objects.create(
        carrier=random.choice(carriers),
        vehicle_info=fake.word(),

        start_location=fake.city(),
        end_location=fake.city(),

        status=random.choice(['planned', 'in_progress', 'completed']),
    )
    deliveries.append(delivery)

print("✅ Deliveries created")

# -----------------------
# 4. ORDERS + ORDER ITEMS
# -----------------------

for _ in range(10):
    seller = random.choice(sellers)
    buyer = random.choice(buyers)
    delivery = random.choice(deliveries)

    order = Order.objects.create(
        seller=seller,
        buyer=buyer,

        pickup_address=fake.address(),
        delivery_address=fake.address(),

        delivery=delivery,

        status=random.choice([
            'created', 'confirmed', 'assigned',
            'picked_up', 'in_transit', 'delivered'
        ]),

        # нові поля
        time_started=timezone.now() if random.choice([True, False]) else None,
        time_finished=timezone.now() if random.choice([True, False]) else None,
        notes=fake.text(max_nb_chars=50),
    )

    # 🔥 створюємо OrderItem замість просто M2M
    selected_products = random.sample(products, random.randint(1, 3))

    for product in selected_products:
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=random.randint(1, 5),
            price=product.price
        )

print("✅ Orders + OrderItems created")

print("🎉 ALL DATA GENERATED SUCCESSFULLY")