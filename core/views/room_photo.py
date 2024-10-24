from rest_framework.viewsets import ModelViewSet

from core.models import RoomPhoto
from core.serializers import RoomPhotoSerializer

class RoomPhotoViewSet(ModelViewSet):
    queryset = RoomPhoto.objects.all()
    serializer_class = RoomPhotoSerializer