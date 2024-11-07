from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from datetime import datetime
from django.db.models import Q, F, ExpressionWrapper, IntegerField
from core.models import Room, RoomAvailability
from core.serializers import RoomSerializer

class AvailableRoomsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')
        guest_count = request.query_params.get('guest_count')
        
        if not start_date_str or not end_date_str or not guest_count: 
            return Response({"error": "Missing parameters."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            guest_count = int(guest_count)
        except ValueError:
            return Response({"error": "Invalid guest count format. It must be an integer."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
            if start_date > end_date:
                return Response({"error": "The start date must be before the ebd date."}, status=status.HTTP_400_BAD_REQUEST)
        except (ValueError, TypeError):
            return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

        unavailable_rooms = RoomAvailability.objects.filter(
            Q(start_date__lte=end_date) & Q(end_date__gte=start_date)
        ).values_list('room_id', flat=True)

        available_rooms = Room.objects.annotate(
            max_capacity=ExpressionWrapper(
                F('single_beds') + F('couple_beds') * 2, output_field=IntegerField()
            )
        ).filter(
            ~Q(id__in=unavailable_rooms),
            max_capacity__gte=guest_count
        )
        
        serializer = RoomSerializer(available_rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)