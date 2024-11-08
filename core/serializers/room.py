from rest_framework.serializers import ModelSerializer

from core.models import Room
from core.serializers import CategorySerializer, RoomPhotoSerializer

class RoomSerializer(ModelSerializer):
    category = CategorySerializer()
    photos = RoomPhotoSerializer(source='roomphoto_set', many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'name', 'single_beds', 'couple_beds', 'price_by_day', 'description', 'category', 'photos']