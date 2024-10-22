from rest_framework.serializers import ModelSerializer

from core.models import Booking

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"