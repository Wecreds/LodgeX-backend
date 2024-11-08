from datetime import datetime
from rest_framework import status, generics
from rest_framework.response import Response
from core.models import Booking, RoomAvailability, Room, BookingRoom
from core.serializers import BookingSerializer
from rest_framework.permissions import IsAuthenticated
from django.db import transaction

class BookingCreateView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    def create(self, request, *args, **kwargs):
        room_id = request.data.get('room_id')
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')
        guest_count = request.data.get('guest_count')

        if not room_id or not start_date or not end_date or not guest_count:
            return Response({"detail": "Room ID, start date, end date, and guest_count are required."}, status=status.HTTP_400_BAD_REQUEST)

        user = request.user

        existing_booking = Booking.objects.filter(user=user, booking_status=Booking.BookingStatus.ACTIVE).first()

        if existing_booking:
            room = Room.objects.get(id=room_id)

            overlapping_availability = RoomAvailability.objects.filter(
                room=room,
                room_status=RoomAvailability.RoomStatus.RESERVED,
                start_date__lt=end_date,
                end_date__gt=start_date
            )

            if overlapping_availability.exists():
                return Response({"detail": "The room is not available for the selected dates."}, status=status.HTTP_400_BAD_REQUEST)

            start_date = datetime.strptime(start_date, "%Y-%m-%d").date() if isinstance(start_date, str) else start_date.date()
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date() if isinstance(end_date, str) else end_date.date()

            RoomAvailability.objects.create(
                room=room,
                start_date=start_date,
                end_date=end_date,
                room_status=RoomAvailability.RoomStatus.RESERVED,
                guest_count=guest_count,
                booking=existing_booking
            )

            BookingRoom.objects.create(room=room, booking=existing_booking)

            return Response(BookingSerializer(existing_booking).data, status=status.HTTP_201_CREATED)

        with transaction.atomic():
            room = Room.objects.get(id=room_id)

            booking = Booking.objects.create(
                user=user,
                booking_status=Booking.BookingStatus.ACTIVE,
                discount_coupon=request.data.get('discount_coupon', None)
            )

            start_date = datetime.strptime(start_date, "%Y-%m-%d").date() if isinstance(start_date, str) else start_date.date()
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date() if isinstance(end_date, str) else end_date.date()

            RoomAvailability.objects.create(
                room=room,
                start_date=start_date,
                end_date=end_date,
                room_status=RoomAvailability.RoomStatus.RESERVED,
                guest_count=guest_count,
                booking=booking
            )

            BookingRoom.objects.create(room=room, booking=booking)

            return Response(BookingSerializer(booking).data, status=status.HTTP_201_CREATED)
