# userapp/urls.py
from django.urls import path
from .views import home, products, contact

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('contact/', contact, name='contact'),
]
