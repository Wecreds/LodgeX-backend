from rest_framework.viewsets import ModelViewSet

from core.models import RoomAvailability
from core.serializers import RoomAvailabilitySerializer

class RoomAvailabilityViewSet(ModelViewSet):
    queryset = RoomAvailability.objects.all()
    serializer_class = RoomAvailabilitySerializer