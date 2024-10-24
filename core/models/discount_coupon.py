from django.db import models
from django.utils import timezone

class DiscountCouponManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(expiration_date__gte=timezone.now().date())

class DiscountCoupon(models.Model):
    code = models.CharField(max_length=10, null=False, unique=True)
    discount_percentage = models.IntegerField(default=0, null=False)
    expiration_date = models.DateField(null=False)
    description = models.CharField(max_length=200, null=True, blank=True, default=None)

    objects = DiscountCouponManager()

    def __str__(self):
        return f"{self.code} - Expiration: {self.expiration_date} ({self.discount_percentage}% Discount)"
    
    class Meta:
        verbose_name = "Discount Coupon"
        verbose_name_plural = "Discount Coupons"
