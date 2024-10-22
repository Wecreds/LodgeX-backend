from rest_framework.serializers import ModelSerializer

from core.models import RoomAvailability

class RoomAvailabilitySerializer(ModelSerializer):
    class Meta:
        model = RoomAvailability
        fields = "__all__"