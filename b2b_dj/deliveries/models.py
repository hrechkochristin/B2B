from django.db import models

class Delivery(models.Model):

    STATUS_CHOICES = [
        ('planned', 'Заплановано'),
        ('in_progress', 'Виконується'),
        ('completed', 'Завершено'),
        ('cancelled', 'Скасовано'),
    ]

    carrier = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='deliveries'
    )

    # можна додати транспорт
    vehicle_info = models.CharField(max_length=255, blank=True)

    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planned')

    departure_time = models.DateTimeField(null=True, blank=True)
    arrival_time = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    notes = models.TextField(blank=True)

    # 🔥 агрегати по всіх замовленнях
    def total_weight(self):
        return sum(order.total_weight() for order in self.orders.all())

    def total_volume(self):
        return sum(order.total_volume() for order in self.orders.all())

    def __str__(self):
        return f"Delivery {self.id}"