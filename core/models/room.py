from django.db import models
from core.models import Promotion, Category

class Room(models.Model):
    single_beds = models.IntegerField()
    couple_beds = models.IntegerField()
    price_by_day = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=400)
    """
    photos = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    """
    promotion = models.ForeignKey(
        Promotion, 
        on_delete=models.PROTECT, 
        null=True, 
        blank=True, 
        default=None
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        default=None
    )


    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = "Promotion"
        verbose_name_plural = "Promotions"