from rest_framework.viewsets import ModelViewSet
from core.models import Lodge, LodgeAmenity, LodgePolicy, LodgePaymentMethod
from core.serializers import (
    LodgeSerializer,
    LodgeAmenitySerializer,
    LodgePolicySerializer,
    LodgePaymentMethodSerializer,
)

class LodgeViewSet(ModelViewSet):
    queryset = Lodge.objects.all()
    serializer_class = LodgeSerializer

class LodgeAmenityViewSet(ModelViewSet):
    queryset = LodgeAmenity.objects.all()
    serializer_class = LodgeAmenitySerializer

class LodgePolicyViewSet(ModelViewSet):
    queryset = LodgePolicy.objects.all()
    serializer_class = LodgePolicySerializer

class LodgePaymentMethodViewSet(ModelViewSet):
    queryset = LodgePaymentMethod.objects.all()
    serializer_class = LodgePaymentMethodSerializer
