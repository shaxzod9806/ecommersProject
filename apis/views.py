from rest_framework.views import APIView
from .serializers import SubCategorySerializer, CategorySerializer, BrandSerializer, ProductSerializer
from .models import Brand, Category, Sub_Category, Product
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser


class BrandAPI(APIView):
    # permission_classes = [IsAdminUser, IsAuthenticated]
    serializer_classes = BrandSerializer
    parser_classes = (MultiPartParser, FormParser)

    param_config = openapi.Parameter(
        'Authorization',
        in_=openapi.IN_HEADER,
        description='enter access token with Bearer word for example: Bearer token ',
        type=openapi.TYPE_STRING
    )

    @swagger_auto_schema(manual_parameters=[param_config])
    def get(self, request):
        brand = Brand.objects.all()
        serializers = BrandSerializer(brand, many=True, context={"request": request})
        return Response(serializers.data)

    @swagger_auto_schema(
        parser_classes=parser_classes,
        request_body=BrandSerializer,
        manual_parameters=[param_config],
    )
    def post(self, request):
        serializer = BrandSerializer(data=request.data, many=False, context={'request': request})
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    brand_id = openapi.Parameter(
        'brand_id', in_=openapi.IN_FORM,
        description='enter brand id',
        type=openapi.TYPE_INTEGER,
    )

    @swagger_auto_schema(request_body=BrandSerializer, manual_parameters=[param_config, brand_id])
    def put(self, request):
        brand_id = request.data['brand_id']
        brand = Brand.objects.get(id=int(brand_id))
        serializer = BrandSerializer(brand, many=False, data=request.data, context={"request": request})
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=[brand_id, param_config], parser_classes=parser_classes)
    def delete(self, request):
        brand_id = request.data['brand_id']
        brand = Brand.objects.get(id=int(brand_id))
        brand.delete()
        return Response({'details': 'brand is deleted'}, status=status.HTTP_200_OK)


class CategoryAPI(APIView):
    permission_classes = [IsAdminUser, IsAuthenticated]
    serializer_classes = CategorySerializer
    parser_classes = (MultiPartParser, FormParser)

    param_config = openapi.Parameter(
        'Authorization',
        in_=openapi.IN_HEADER,
        description='enter access token with Bearer word for example: Bearer token ',
        type=openapi.TYPE_STRING
    )

    @swagger_auto_schema(manual_parameters=[param_config])
    def get(self, request):
        category = Category.objects.all()
        serializers = CategorySerializer(category, many=True)
        return Response(serializers.data)

    @swagger_auto_schema(
        parser_classes=parser_classes,
        request_body=CategorySerializer,
        manual_parameters=[param_config],
    )
    def post(self, request):

        serializer = CategorySerializer(data=request.data, many=False)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    category_id = openapi.Parameter(
        'category_id', in_=openapi.IN_FORM,
        description='enter brand id',
        type=openapi.TYPE_INTEGER,
    )

    @swagger_auto_schema(request_body=CategorySerializer, manual_parameters=[param_config, category_id])
    def put(self, request):

        category_id = request.data['category_id']
        category = Category.objects.get(id=int(category_id))
        serializer = CategorySerializer(category, many=False, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=[category_id, param_config], parser_classes=parser_classes)
    def delete(self, request):
        category_id = request.data['category_id']
        category = Category.objects.get(id=int(category_id))
        category.delete()
        return Response({'details': 'brand is deleted'}, status=status.HTTP_200_OK)
