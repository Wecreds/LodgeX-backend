from rest_framework.viewsets import ModelViewSet

from core.models import Payment
from core.serializers import PaymentSerializer

class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer