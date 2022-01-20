from django.urls import path, include
from .views import UserProfile
from .views import ProfileRegister

urlpatterns = [
    path('user_profile', UserProfile.as_view(), name='user_profile'),
    path('register_profile', ProfileRegister.as_view(), name='register_profile'),
]
