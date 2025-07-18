from rest_framework import viewsets
from .serializers import ListingSerializer, BookingSerializer
from .models import Listing, Booking

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer