# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from rest_framework.parsers import MultiPartParser, FormParser
# from .serializers import OrderSerializer
# from drf_yasg import openapi
# from drf_yasg.utils import swagger_auto_schema
# from .models import Order
# from rest_framework import status
#
#
# # Create your views here.
#
# class OrderApi(APIView):
#     permission_classes = [IsAdminUser, IsAuthenticated]
#     serializer_class = OrderSerializer
#     parser_classes = (MultiPartParser, FormParser)
#
#     param_config = openapi.Parameter(
#         'Authorization',
#         in_=openapi.IN_HEADER,
#         description='enter access token with Bearer word for example: Bearer token',
#         type=openapi.TYPE_STRING,
#     )
#
#     @swagger_auto_schema(manual_parameters=[param_config])
#     def get(self, request):
#         order = Order.objects.all()
#         serializers = OrderSerializer(order, many=True)
#         return Response(serializers.data)
#
#     @swagger_auto_schema(
#         manual_parameters=[param_config],
#         parser_classes=parser_classes,
#         request_body=OrderSerializer,
#     )
#     def post(self, request):
#         serializer = OrderSerializer(data=request.data, many=False)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     order_id = openapi.Parameter(
#         'order_id', in_=openapi.IN_FORM,
#         description='enter ordering id',
#         type=openapi.TYPE_INTEGER,
#     )
#
#     @swagger_auto_schema(request_body=OrderSerializer, manual_parameters=[param_config, order_id])
#     def put(self, request):
#         order_id = request.data['order_id']
#         order = Order.objects.get(id=int(order_id))
#         serializer = OrderSerializer(order, many=False, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     @swagger_auto_schema(manual_parameters=[param_config, order_id], parser_classes=parser_classes)
#     def delete(self, request):
#         order_id = request.data['order_id']
#         order = Order.objects.get(id=int(order_id))
#         order.delete()
#         return Response({'detail': 'ordering is deleted'}, status=status.HTTP_200_OK)
