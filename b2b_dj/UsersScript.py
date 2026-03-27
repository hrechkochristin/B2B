# seed_script.py
import os
import django
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'b2b_dj.settings')
django.setup()

from users.models import User
from orders.models import Order
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

sellers = [u for u in users if u.is_seller]
buyers = [u for u in users if u.is_buyer]
carriers = [u for u in users if u.is_carrier]

# fallback щоб не впасти
if not sellers: sellers = users
if not buyers: buyers = users
if not carriers: carriers = users

# -----------------------
# 2. PRODUCTS
# -----------------------

products = []

for _ in range(10):
    product = Product.objects.create(
        seller=random.choice(sellers),
        name=fake.word(),

        origin_location=fake.city(),
        origin_storage=fake.company(),

        quantity=random.randint(1, 50),
        weight=round(random.uniform(0.5, 20), 2),
        volume=round(random.uniform(0.01, 2), 2),

        is_perishable=random.choice([True, False]),
        is_fragile=random.choice([True, False]),
        is_animal_origin=random.choice([True, False]),
        is_hazardous=random.choice([True, False]),

        temperature_regime=random.choice([
            'deep_frozen', 'frozen', 'cold_chain',
            'chilled', 'ambient', 'heated', 'no_control'
        ]),
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
# 4. ORDERS
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
        ])
    )

    # додаємо 1-3 продукти в ордер
    selected_products = random.sample(products, random.randint(1, 3))
    order.products.set(selected_products)

print("✅ Orders created")

print("🎉 ALL DATA GENERATED SUCCESSFULLY")
print("Hello world!")