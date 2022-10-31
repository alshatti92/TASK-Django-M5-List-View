from .models import Booking, Flight
from rest_framework.generics import ListAPIView
from .serializer import FlightListSerializer, BookingsListSerializer
# to filter the time zone to show the coming booking only, u need to import timezone
from django.utils import timezone


class FlightsListViews(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer

class BookingsListViews(ListAPIView):
    queryset = Booking.objects.filter(date__gt=timezone.now)
    serializer_class = BookingsListSerializer
