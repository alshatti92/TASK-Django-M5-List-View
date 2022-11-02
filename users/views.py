from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializer import UserCreateSeriliazer, UserLoginSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

# Create your views here.
class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSeriliazer


class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        data = request.data
        serializer = UserLoginSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            