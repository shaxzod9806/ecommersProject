from rest_framework import serializers
from .models import Product, Category, Sub_Category, Brand


class BrandSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField('get_photo_url')

    class Meta:
        model = Brand
        fields = '__all__'

    def get_photo_url(self, obj):
        request = self.context.get("request")
        photo_url = obj.brand_image.url
        return request.build_absolute_uri(photo_url)


class CategorySerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField('get_photo_url')

    class Meta:
        model = Category
        fields = '__all__'

    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.image.url
        return request.build_absolute_uri(photo_url)


class CategorySerializerUz(serializers.ModelSerializer):
    name = serializers.SerializerMethodField('name_uz')
    description = serializers.SerializerMethodField('description_uz'),

    class Meta:
        model = Category
        fields = '__all__'

    def description_uz(self, obj):
        description = obj.description_uz
        return description

    def name_uz(self, obj):
        name = obj.name_uz
        return name

    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.image.url
        return request.build_absolute_uri(photo_url)


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
