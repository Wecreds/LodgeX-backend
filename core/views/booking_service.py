from rest_framework.viewsets import ModelViewSet

from core.models import BookingService
from core.serializers import BookingServiceSerializer

class BookingServiceViewSet(ModelViewSet):
    queryset = BookingService.objects.all()
    serializer_class = BookingServiceSerializer