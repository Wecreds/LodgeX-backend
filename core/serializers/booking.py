from rest_framework import serializers
from core.models import Booking, RoomAvailability, Room
from .room_availability import RoomAvailabilitySerializer

class BookingSerializer(serializers.ModelSerializer):
    room_availability = RoomAvailabilitySerializer(source='roomavailability_set', many=True, read_only=True)
    user_name = serializers.CharField(source='user.name', read_only=True)
    booking_status = serializers.CharField(source='get_booking_status_display')
    
    room_id = serializers.IntegerField(write_only=True)  
    start_date = serializers.DateField(write_only=True)  
    end_date = serializers.DateField(write_only=True) 

    class Meta:
        model = Booking
        fields = ['id', 'booking_status', 'booking_date', 'discount_coupon', 'user_name', 'room_availability', 'room_id', 'start_date', 'end_date']
    
    def validate(self, data):
        room = Room.objects.get(id=data['room_id'])
        start_date = data['start_date']
        end_date = data['end_date']

        room_availability = RoomAvailability.objects.filter(
            room=room,
            start_date__lt=end_date,
            end_date__gt=start_date,
            room_status=RoomAvailability.RoomStatus.RESERVED
        )

        if room_availability.exists():
            raise serializers.ValidationError("The room is not available for the selected dates.")

        return data

    def create(self, validated_data):
        room = Room.objects.get(id=validated_data['room_id'])
        booking = Booking.objects.create(
            user=validated_data['user'],
            booking_status=Booking.BookingStatus.ACTIVE,
            booking_date=validated_data['booking_date'],
            discount_coupon=validated_data.get('discount_coupon', None)
        )

        RoomAvailability.objects.create(
            room=room,
            start_date=validated_data['start_date'],
            end_date=validated_data['end_date'],
            room_status=RoomAvailability.RoomStatus.RESERVED,
            booking=booking
        )

        return booking
