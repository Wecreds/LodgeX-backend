from rest_framework.viewsets import ModelViewSet

from core.models import Booking
from core.serializers import BookingSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer