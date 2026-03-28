from django.db import models

class Product(models.Model):
    TEMPERATURE_CHOICES = [
        ('deep_frozen', 'Глибока заморозка (-25°C до -18°C)'), 
        ('frozen', 'Заморозка (-18°C до -10°C)'),
        
        ('cold_chain', 'Холодний ланцюг (+2°C до +8°C)'),
        ('chilled', 'Охолоджене (+8°C до +15°C)'),
        
        ('ambient', 'Кімнатна температура (+15°C до +25°C)'),
        ('heated', 'З підігрівом (вище +25°C)'),
        
        ('no_control', 'Без контролю температури'), 
    ]

    CATEGORY_CHOICES = [
    # Продукти харчування
    ('bakery', 'Хлібобулочні та кондитерські вироби'),
    ('dairy', 'Молочні продукти та яйця'),
    ('meat_fish', 'М’ясо, птиця та риба'),
    ('fruits_veg', 'Овочі та фрукти'),
    ('grocery', 'Бакалія та консерви'),
    ('beverages', 'Напої (безалкогольні та алкогольні)'),
    
    # Побутові та інші товари
    ('household', 'Побутова хімія та товари для дому'),
    ('hygiene', 'Гігієна та косметика'),
    ('electronics', 'Електроніка та техніка'),
    ('apparel', 'Одяг та взуття'),
    ('pet_supplies', 'Товари для тварин'),
    
    # Інше
    ('other', 'Інше / Різне'),
]

    STOCK_CHOISES = [
        ('in_stock', 'В наявності'),
        ('out_of_stock', 'Немає в наявності'),
        ('pre_order', 'Під замовлення'),
    ]

    seller = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='products')

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    origin_location = models.CharField(max_length=255)
    origin_storage = models.CharField(max_length=255, blank=True)

    quantity = models.IntegerField()
    stock = models.CharField(max_length=20, choices=STOCK_CHOISES, default='in_stock')
    weight = models.FloatField(help_text="Вага однієї одиниці")
    volume = models.FloatField(help_text="Об'єм однієї одиниці")

    is_perishable = models.BooleanField(default=False)
    is_fragile = models.BooleanField(default=False)
    is_animal_origin = models.BooleanField(default=False)
    is_hazardous = models.BooleanField(default=False)

    temperature_regime = models.CharField(max_length=20, choices=TEMPERATURE_CHOICES, default='no_control')

    description = models.TextField(blank=True)

    def total_weight(self):
        return self.quantity * self.weight

    def total_volume(self):
        return self.quantity * self.volume

    def __str__(self):
        return self.name