from django.urls import path
from .views import CustomerAPI,CustomerRegister

urlpatterns = [
    path('customer/', CustomerAPI.as_view(), name='customer'),
    path('customer_register/', CustomerRegister.as_view(), name='customer_register'),
]
