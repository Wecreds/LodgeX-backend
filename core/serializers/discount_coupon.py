from rest_framework.serializers import ModelSerializer

from core.models import DiscountCoupon

class DiscountCouponSerializer(ModelSerializer):
    class Meta:
        model = DiscountCoupon
        fields = "__all__"