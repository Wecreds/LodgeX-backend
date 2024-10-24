from django.db import models

class Promotion(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, default="No Promotion Name Given")
    discount_percentage = models.IntegerField()
    expiration_date = models.DateField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} - Expiration: {self.expiration_date} ({self.discount_percentage}% Discount)"
    
    class Meta:
        verbose_name = "Promotion"
        verbose_name_plural = "Promotions"