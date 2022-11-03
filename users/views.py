from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from flights.models import Flight

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

    def post(self, request):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)


class BookingCreateAPIView(CreateAPIView):
    serializer_class = BookingCreateSerializer
    

    def perform_create(self, serializer):
        flight_id = self.kwargs['flight_id']
        flight = Flight.objects.get(id=flight_id)
        serializer.save(user=self.request.user, flight=flight)
       

        print(flight)

        
   