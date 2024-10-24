from django.db import models
from core.models import Category

class Room(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, default="No room name given.")
    single_beds = models.IntegerField(null=False, blank=False, default=0)
    couple_beds = models.IntegerField(null=False, blank=False, default=0)
    price_by_day = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False, default=0)
    description = models.CharField(max_length=400, null=False, blank=False, default="No description given.")
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
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        default=None
    )

    def __str__(self):
        return f"{self.name} - {self.category.name}"
    
    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"