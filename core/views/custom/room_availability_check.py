# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from datetime import datetime
from django.db.models import Q
from core.models import Room, RoomAvailability

class RoomAvailabilityCheckView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')
        room_id = request.query_params.get('room_id')

        if not room_id or not start_date_str or not end_date_str: 
            return Response({"detail": "Missing parameters."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            room_id = int(room_id)
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
            if start_date > end_date:
                return Response({"detail": "The arrival date must be before the departure date."}, status=status.HTTP_400_BAD_REQUEST)
        except (ValueError, TypeError):
            return Response({"detail": "Invalid data format or room_id. Use YYYY-MM-DD for data and an integer for room_id."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            room = Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            return Response({"detail": "Quarto não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        is_unavailable = RoomAvailability.objects.filter(Q(room=room) & Q(start_date__lte=end_date) & Q(end_date__gte=start_date)).exists()

        if not is_unavailable:
            return Response({"available": True}, status=status.HTTP_200_OK)
        else:
            return Response({"available": False}, status=status.HTTP_200_OK)
