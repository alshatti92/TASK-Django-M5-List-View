from urllib import response
from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from flights.serializer import BookingCreateSerializer
from .serializer import UserCreateSeriliazer, UserLoginSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

# Create your views here.
class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSeriliazer


class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        serializer = UserLoginSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return response(valid_data, status=HTTP_200_OK)
        return response(serializer.errors, HTTP_400_BAD_REQUEST)


class BookingCreateAPIView(CreateAPIView):
    serializer_class = BookingCreateSerializer
   