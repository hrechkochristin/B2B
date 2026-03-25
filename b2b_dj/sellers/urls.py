from django.urls import include, path
from . import views

urlpatterns = [
    path("",views.main, name="main"),
    path("seller_new_offers/", views.seller_new_offers, name="seller_new_offers"),
    path("seller_product/", views.seller_product, name="seller_product"),
    path("seller_order/", views.seller_order, name="seller_order"), 
    path("seller_buyers/", views.seller_buyers, name="seller_buyers"),
    path("seller_carriers/", views.seller_carriers, name="seller_carriers"),
    path("seller_storage/", views.seller_storage, name="seller_storage"),
    
]