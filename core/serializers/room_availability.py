from rest_framework.serializers import ModelSerializer, CharField

from core.models import RoomAvailability
from core.serializers.room import RoomSerializer

class RoomAvailabilitySerializer(ModelSerializer):
    room = RoomSerializer()
    room_status = CharField(source='get_room_status_display') 

    class Meta:
        model = RoomAvailability
        fields = ['start_date', 'end_date', 'room_status', 'reason', 'room', 'guest_count']