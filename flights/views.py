from .models import Booking, Flight
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from .serializer import FlightListSerializer, BookingsListSerializer, BookingDetailsSerializer, BookingCreateSerializer
# to filter the time zone to show the coming booking only, u need to import timezone
from django.utils import timezone


class FlightsListViews(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer

class BookingsListViews(ListAPIView):
    queryset = Booking.objects.filter(date__gt=timezone.now())
    serializer_class = BookingsListSerializer

class BookingDetailsViews(RetrieveAPIView):
    queryset= Booking.objects.all()
    serializer_class= BookingDetailsSerializer
    lookup_field= "id"
    lookup_url_kwarg= "booking_id"

class BookingCreateView(CreateAPIView):
    serializer_class= BookingCreateSerializer
    
class BookingUpdateView(UpdateAPIView):
    queryset= Booking.objects.all()
    serializer_class= BookingCreateSerializer
    lookup_field= "id"
    lookup_url_kwarg= "booking_id"

class BookingDeleteView(DestroyAPIView):
    queryset= Booking.objects.all()
    serializer_class= BookingsListViews
    lookup_field= "id"
    lookup_url_kwarg= "booking_id"