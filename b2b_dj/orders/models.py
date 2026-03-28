from django.db import models

class Order(models.Model):

    STATUS_CHOICES = [
        ('created', 'Створено'),
        ('confirmed', 'Підтверджено'),
        ('assigned', 'Призначено в доставку'),
        ('picked_up', 'Забрано'),
        ('in_transit', 'В дорозі'),
        ('delivered', 'Доставлено'),
        ('cancelled', 'Скасовано'),
    ]

    seller = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='orders_as_seller'
    )

    buyer = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='orders_as_buyer'
    )

    # 🔥 ВАЖЛИВО: products.Product
    products = models.ManyToManyField(
        'products.Product',
        related_name='orders'
    )

    price = models.DecimalField(max_digits=10, decimal_places=2)    

    # 📍 маршрут
    pickup_address = models.CharField(max_length=255)
    delivery_address = models.CharField(max_length=255)

    # 🔥 ВАЖЛИВО: deliveries.Delivery
    delivery = models.ForeignKey(
        'deliveries.Delivery',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='created'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    time_started = models.DateTimeField(null=True, blank=True)
    time_finished = models.DateTimeField(null=True, blank=True)

    notes = models.TextField(blank=True)

    def total_weight(self):
        return sum(p.total_weight() for p in self.products.all())

    def total_volume(self):
        return sum(p.total_volume() for p in self.products.all())

    def __str__(self):
        return f"Order {self.id}"