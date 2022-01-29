from django.db import models
from customer.models import Customer
from seller.models import Profile
from apis.models import Product


# Create your models here.
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    customer_long = models.FloatField(null=True)
    customer_lat = models.FloatField(null=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    order_price = models.FloatField(null=True)
    is_cancelled = models.BooleanField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
