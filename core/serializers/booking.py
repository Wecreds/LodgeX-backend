from rest_framework.serializers import ModelSerializer, CharField
from core.models import Booking
from .room_availability import RoomAvailabilitySerializer 

class BookingSerializer(ModelSerializer):
    room_availability = RoomAvailabilitySerializer(source='roomavailability_set', many=True, read_only=True)
    user_name = CharField(source='user.name', read_only=True)
    booking_status = CharField(source='get_booking_status_display')

    class Meta:
        model = Booking
        fields = ['id', 'booking_status', 'booking_date', 'discount_coupon', 'user_name', 'room_availability']
