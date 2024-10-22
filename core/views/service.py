from rest_framework.viewsets import ModelViewSet

from core.models import Service
from core.serializers import ServiceSerializer

class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer