from django.db import models

class Product(models.Model):
    TEMPERATURE_CHOICES = [
    # Заморозка
    ('deep_frozen', 'Глибока заморозка (-25°C до -18°C)'), 
    ('frozen', 'Заморозка (-18°C до -10°C)'),
    
    # Охолодження
    ('cold_chain', 'Холодний ланцюг (+2°C до +8°C)'), # Стандарт для фармакології та молочки
    ('chilled', 'Охолоджене (+8°C до +15°C)'), # Овочі, фрукти
    
    # Контрольоване середовище
    ('ambient', 'Кімнатна температура (+15°C до +25°C)'),
    ('heated', 'З підігрівом (вище +25°C)'), # Для деяких видів клею або кондитерської сировини
    
    # Без контролю
    ('no_control', 'Без контролю температури'), 
    ]

    seller = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='products')

    name = models.CharField(max_length=255)

    origin_location = models.CharField(max_length=255)
    origin_storage = models.CharField(max_length=255, blank=True)

    quantity = models.IntegerField()
    weight = models.FloatField(help_text="Вага однієї одиниці")
    volume = models.FloatField(help_text="Об'єм однієї одиниці")

    is_perishable = models.BooleanField(default=False)
    is_fragile = models.BooleanField(default=False)
    is_animal_origin = models.BooleanField(default=False)
    is_hazardous = models.BooleanField(default=False)

    temperature_regime = models.CharField(max_length=20)

    expiration_date = models.DateField(null=True, blank=True)

    def total_weight(self):
        return self.quantity * self.weight

    def total_volume(self):
        return self.quantity * self.volume

    def __str__(self):
        return self.name