from django.db import models
from django.utils import timezone

class PromotionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(expiration_date__gte=timezone.now().date())
class Promotion(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, default="No Promotion Name Given")
    discount_percentage = models.IntegerField()
    expiration_date = models.DateField()
    description = models.CharField(max_length=200)

    objects = PromotionManager()

    def __str__(self):
        return f"{self.name} - Expiration: {self.expiration_date} ({self.discount_percentage}% Discount)"
    
    class Meta:
        verbose_name = "Promotion"
        verbose_name_plural = "Promotions"