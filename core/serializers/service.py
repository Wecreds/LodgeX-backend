from rest_framework.serializers import ModelSerializer

from core.models import Service

class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"