from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializer import UserCreateSeriliazer

# Create your views here.
class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSeriliazer