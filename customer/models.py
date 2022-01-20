from django.db import models
from index.models import User


# Create your models here.

class Customer(models.Model):
    phone_number = models.CharField(max_length=13)
    customer_address = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.user
