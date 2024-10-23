from rest_framework.serializers import ModelSerializer

from core.models import Cancellation

class CancellationSerializer(ModelSerializer):
    class Meta:
        model = Cancellation
        fields = "__all__"