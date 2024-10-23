from rest_framework.serializers import ModelSerializer

from core.models import BookingRoom

class BookingRoomSerializer(ModelSerializer):
    class Meta:
        model = BookingRoom
        fields = "__all__"