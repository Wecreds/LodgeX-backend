from rest_framework.viewsets import ModelViewSet

from core.models import DiscountCoupon
from core.serializers import DiscountCouponSerializer

class DiscountCouponViewSet(ModelViewSet):
    queryset = DiscountCoupon.objects.all()
    serializer_class = DiscountCouponSerializer