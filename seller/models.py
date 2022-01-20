from django.db import models
from index.models import User

upload_path = 'seller/documents'


# Create your models here.
class Profile(models.Model):
    phone_number = models.CharField(max_length=255, null=True)
    organization = models.CharField(max_length=255, null=True)
    office_address = models.TextField()
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.username
