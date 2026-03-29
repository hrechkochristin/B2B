from django.db import models
from django.contrib.auth.models import User

class CartItem(models.Model):
    buyer = models.ForeignKey(
        'users.User', 
        on_delete=models.CASCADE, 
        related_name='cart_entries' 
    )
    
    order = models.ForeignKey(
        'orders.Order',
        on_delete=models.CASCADE, 
        related_name='items', 
        null=True, 
        blank=True
    )
    
    product = models.ForeignKey(
        'products.Product', 
        on_delete=models.CASCADE,
        related_name='order_lines'
    )

    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} (Order: {self.order_id})"