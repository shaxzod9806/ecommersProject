from django.contrib import admin

from seller.models import Profile
from seller.models import User

# Register your models here.
admin.site.register(Profile)
admin.site.register(User)

