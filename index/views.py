import random

from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import CreateAPIView
from seller.serializer import UserSerializer
from drf_yasg.utils import swagger_auto_schema
from index.models import User
from utilits.sms import send_sms
from utilits.models import SMS
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg import openapi


# Create your views here.
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['usertype'] = self.user.user_type
        data['email'] = self.user.email
        data['firstname'] = self.user.first_name
        data['lastname'] = self.user.last_name
        data['user_id'] = self.user.id

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserRegister(CreateAPIView):
    serializer_class = UserSerializer
    http_method_names = ['post']

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,

            properties={
                'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='The desc'),
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='The desc'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='The desc'),
                'user_type': openapi.Schema(type=openapi.TYPE_INTEGER, description='The desc'),
            }
        ))
    def post(self, request):
        data = request.data
        random_number = random.randrange(10000, 99999)
        user = User.objects.create(
            first_name=data['first_name'],
            username=data['username'],
            password=data['password'],
            user_type=data['user_type'],
            is_active=False,
            activation_code=random_number
        )
        serializer = UserSerializer(user, many=False)
        sms_itself = SMS.objects.create(
            phone_number=user.username,
            text=random_number
        )
        if not user.is_active:
            send_sms(
                number=sms_itself.phone_number,
                text=sms_itself.text,
                sms_id=sms_itself.id
            )
        sms_itself.is_sent = 1
        return Response(serializer.data)


class VerifyUser(APIView):
    user_id = openapi.Parameter(
        'user_id',
        in_=openapi.IN_QUERY,
        description='Enter user id to verify the user ',
        type=openapi.TYPE_INTEGER
    )
    verification_code = openapi.Parameter(
        'verification_code',
        in_=openapi.IN_QUERY,
        description='Enter verification_code to verify the user ',
        type=openapi.TYPE_INTEGER
    )

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,

            properties={
                'user_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='The desc'),
                'verification_code': openapi.Schema(type=openapi.TYPE_INTEGER, description='The desc'),
            }
        ))
    def post(self, request):
        user_id = request.GET.get('user_id')
        verification_code = request.GET.get('verification_code')
        user_itself = User.objects.get(id=user_id)
        print('if out')
        if user_itself.is_active:
            print('user is alredy activated')
            return Response('user is alredy activated')
        if int(verification_code) != int(user_itself.activation_code):
            return Response('activation_code is wrong')
        user_itself.is_active = True
        user_itself.save()
        return Response('user is successfully activated')
