from .models import Booking, Flight
from rest_framework.generics import ListAPIView
from .serializer import FlightListSerializer, BookingsListSerializer


class FlightsListViews(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer

class BookingsListViews(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingsListSerializer
