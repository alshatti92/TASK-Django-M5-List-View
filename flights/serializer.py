from dataclasses import fields
from rest_framework import serializers
from .models import Flight, Booking


class FlightListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ["id", "destination", "time", "price"]


class BookingsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["flight", "date", "id"]


class BookingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "flight", "date", "passengers"]


class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Booking
        fields= ["passengers" , "date"]
