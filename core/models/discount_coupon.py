from django.db import models

class DiscountCoupon(models.Model):
    code = models.CharField(max_length=10, null=False, blank=False, unique=True)
    discount_percentage = models.IntegerField(default=0, null=False, blank=False)
    expiration_date = models.DateField(null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False, default="No description given.")

    def __str__(self):
        return f"{self.code} - Expiration: {self.expiration_date} ({self.discount_percentage}% Discount)"
    
    class Meta:
        verbose_name = "Discount Coupon"
        verbose_name_plural = "Discount Coupons"
