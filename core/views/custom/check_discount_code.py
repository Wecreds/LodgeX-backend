from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import DiscountCoupon
from django.utils import timezone

class CheckDiscountCouponView(APIView):
    def get(self, request, code, *args, **kwargs):
        try:
            discount_coupon = DiscountCoupon.objects.get(code=code, expiration_date__gte=timezone.now().date())
            return Response({
                "detail": "Valid Coupon" 
            }, status=status.HTTP_200_OK)
        except DiscountCoupon.DoesNotExist:
            return Response({"detail": "Coupon not found or expired."}, status=status.HTTP_404_NOT_FOUND)
