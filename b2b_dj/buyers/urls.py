from django.urls import include, path
from . import views

urlpatterns = [
    path("",views.main, name="main"),
    path("buyer_sellers/", views.buyer_sellers, name='buyer_sellers'),
    path("buyer_catalog/", views.buyer_catalog, name='buyer_catalog'),
    path("buyer_orders/", views.buyer_orders, name='buyer_orders'),
    path("buyer_cart/", views.cart_view, name='buyer_cart'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
]