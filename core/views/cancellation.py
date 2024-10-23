from rest_framework.viewsets import ModelViewSet

from core.models import Cancellation
from core.serializers import CancellationSerializer

class CancellationViewSet(ModelViewSet):
    queryset = Cancellation.objects.all()
    serializer_class = CancellationSerializer