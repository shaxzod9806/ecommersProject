from django.urls import path
from .views import OrderApi

urlpatterns = [
    path('ordering/', OrderApi.as_view(), name='ordering')
]
