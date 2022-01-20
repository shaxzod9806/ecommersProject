from django.db import models
from index.models import User

# Create your views here.
upload_path_category = 'Category/'
upload_path_sub_category = 'SubCategory/'
upload_path_products = 'Product/'
upload_path_brand_image = 'Product/brand/'


class Category(models.Model):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    description_uz = models.TextField()
    description_ru = models.TextField()
    description_en = models.TextField()
    image = models.ImageField(upload_to=upload_path_category)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # created_by=models.ForeignKey(User)
    # updated_by=models.ForeignKey(User)

    def __str__(self):
        return self.name_uz


class Sub_Category(models.Model):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    description_uz = models.TextField()
    description_ru = models.TextField()
    description_en = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    image = models.ImageField(upload_to=upload_path_sub_category)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # created_by=models.ForeignKey(User)
    # updated_by=models.ForeignKey(User)

    def __str__(self):
        return self.name_uz


class Product(models.Model):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to=upload_path_products)
    stars = models.SmallIntegerField(default=0)
    is_on_sale = models.BooleanField(default=False)
    description_uz = models.TextField(blank=True)
    description_ru = models.TextField(blank=True)
    description_en = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True,
                                   related_name='pruducts_created',
                                   related_query_name='pruduct_created'
                                   )

    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True,
                                   related_name='pruducts_updated',
                                   related_query_name='pruduct_updated'
                                   )

    def __str__(self):
        return self.name


class Brand(models.Model):
    brand_name = models.CharField(max_length=255)
    brand_image = models.ImageField(upload_to=upload_path_brand_image)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand_name
