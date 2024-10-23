from rest_framework.viewsets import ModelViewSet

from core.models import BookingRoom
from core.serializers import BookingRoomSerializer

class BookingRoomViewSet(ModelViewSet):
    queryset = BookingRoom.objects.all()
    serializer_class = BookingRoomSerializer