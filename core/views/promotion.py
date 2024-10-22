from rest_framework.viewsets import ModelViewSet

from core.models import Promotion
from core.serializers import PromotionSerializer

class PromotionViewSet(ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer