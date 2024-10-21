from django.db import models

class DiscountCoupon(models.Model):
    code = models.CharField(max_length=10, null=False)
    discount_percentage = models.IntegerField(default=0, null=False)
    expiration_date = models.DateField(null=False)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.code