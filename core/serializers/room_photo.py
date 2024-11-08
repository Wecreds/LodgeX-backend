from rest_framework.serializers import ModelSerializer

from core.models import RoomPhoto

class RoomPhotoSerializer(ModelSerializer):
    class Meta:
        model = RoomPhoto
        fields = "__all__"
        depth = 1