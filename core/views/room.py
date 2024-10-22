from rest_framework.viewsets import ModelViewSet

from core.models import Room
from core.serializers import RoomSerializer

class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer