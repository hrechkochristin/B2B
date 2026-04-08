from django.urls import include, path
from . import views

urlpatterns = [
    path("",views.main, name="main"),
    path("carrier_sellers/", views.carrier_sellers, name='carrier_sellers'),
    path("carrier_deliveries/", views.carrier_deliveries, name='carrier_deliveries'),
    path("carrier_orders/", views.carrier_orders, name='carrier_orders'),
    path("carrier_transport/", views.carrier_transport, name='carrier_transport'),
]