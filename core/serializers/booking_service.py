from rest_framework.serializers import ModelSerializer

from core.models import BookingService

class BookingServiceSerializer(ModelSerializer):
    class Meta:
        model = BookingService
        fields = "__all__"