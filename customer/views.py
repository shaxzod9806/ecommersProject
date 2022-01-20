from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import CustomerSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .models import Customer
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from .models import User
from rest_framework import status


# Create your views here.

class CustomerAPI(APIView):
    permission_classes = [IsAdminUser, IsAuthenticated]

    serializer_class = CustomerSerializer
    parser_classes = (MultiPartParser, FormParser)

    param_config = openapi.Parameter(
        'Authorization',
        in_=openapi.IN_HEADER,
        description='enter access token with Bearer token:example Bearer token',
        type=openapi.TYPE_STRING
    )

    @swagger_auto_schema(manual_parameters=[param_config])
    def get(self, request):
        user = request.data
        customer = Customer.objects.all()
        user_serializer = UserSerializer(user, many=True)
        customer_serializer = CustomerSerializer(customer, many=True)
        data = {'user': user_serializer.data, 'profile': customer_serializer.data}
        return Response(data)


class CustomerRegister(CreateAPIView):
    serializer_class = CustomerSerializer
    http_method_names = ['post']

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='The desc'),
            'customer_address': openapi.Schema(type=openapi.TYPE_STRING, description='The desc'),
            'user_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='The desc'),
        }
    ))
    def post(self, request):
        data = request.data
        # try:
        user = User.objects.get(id=data['user_id'])
        customer = Customer.objects.create(
            phone_number=data['phone_number'],
            customer_address=data['customer_address'],
            user=user
        )
        serializer = CustomerSerializer(customer, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
