from django.shortcuts import render
from rest_framework import generics
from .serializers import FlightSerializer, PassengerSerializer, BookingSerializer, HotelSerializer, CarRentalSerializer, DiscountSerializer
from .models import Flight, Passenger, Booking, Hotel, CarRental,Discount

class FlightListCreateView(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class PassengerListCreateView(generics.ListCreateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class HotelListCreateView(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class CarRentListCrateView(generics.ListCreateAPIView):
    queryset = CarRental.objects.all()
    serializer_class = CarRentalSerializer


class DiscountListCreateView(generics.ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


