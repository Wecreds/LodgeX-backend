from rest_framework import status, generics
from rest_framework.response import Response
from core.models import Booking, RoomAvailability
from core.serializers import BookingSerializer
from rest_framework.permissions import IsAuthenticated

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

        if not room_id or not start_date or not end_date:
            return Response({"detail": "Room ID, start date, and end date are required."}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)
