# UsersScript.py
import random
from faker import Faker
from users.models import User  # твоя модель користувача

fake = Faker()

# Створюємо 10 фантомних користувачів
for _ in range(10):
    username = fake.user_name()
    email = fake.email()
    password = fake.password(length=12)  # справжній випадковий пароль

    # Випадкові ролі для трьох полів
    is_seller = random.choice([True, False])
    is_buyer = random.choice([True, False])
    is_carrier = random.choice([True, False])

    # Створюємо користувача
    user = User(
        username=username,
        email=email,
        is_seller=is_seller,
        is_buyer=is_buyer,
        is_carrier=is_carrier
    )
    user.set_password(password)  # хешуємо пароль
    user.save()

    print(f"Created user: {username}, email: {email}, password: {password}, "
          f"roles: [seller={is_seller}, buyer={is_buyer}, carrier={is_carrier}]")