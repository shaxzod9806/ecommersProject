from django.urls import path
from .views import BrandAPI,CategoryAPI

urlpatterns = [
    path('brands/', BrandAPI.as_view(), name='product_brands'),
    path('category/', CategoryAPI.as_view(), name='product_category')
]

