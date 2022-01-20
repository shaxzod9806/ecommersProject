from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'admin'),
        (2, 'manager'),
        (3, 'seller'),
        (4, 'customer'),
    )
    user_type = models.PositiveIntegerField(choices=USER_TYPE_CHOICES, default=4)
    activation_code = models.IntegerField(null=True, blank=True)
