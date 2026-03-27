from django.db import models

class Order(models.Model):
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

    STATUS_CHOICES = [
        ('pending', 'Очікує'),
        ('in_progress', 'В дорозі'),
        ('delivered', 'Доставлено'),
        ('cancelled', 'Скасовано'),
    ]

    # Учасники
    seller = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='orders_as_seller', null=True, blank=True)
    buyer = models.ForeignKey('users.User', on_delete=models.SET_NULL, related_name='orders_as_buyer', null=True, blank=True)

    # Фізичні параметри
    weight = models.FloatField(help_text="Вага в кг")
    volume = models.FloatField(help_text="Об'єм в м3")
    
    # Властивості вантажу
    is_perishable = models.BooleanField("Швидкопсувний", default=False)
    is_fragile = models.BooleanField("Крихкий", default=False)
    is_animal_origin = models.BooleanField("Тваринного походження", default=False)
    is_hazardous = models.BooleanField("Небезпечний (ADR)", default=False)
    temperature_regime = models.CharField(
        max_length=20, 
        choices=TEMPERATURE_CHOICES, 
        default='ambient'
    )
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='pending'
    )
    
    # Розміщення
    gps_location = models.CharField(max_length=255, blank=True)

    # Терміни та логістика
    time_started = models.DateTimeField(null=True, blank=True)
    time_finished = models.DateTimeField(null=True, blank=True)
    
    # Опис та нотатки
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Order {self.id} ({self.weight}kg)"