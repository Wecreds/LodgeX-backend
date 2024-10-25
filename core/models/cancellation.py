from django.db import models
from core.models import Booking
from django.utils import timezone

class Cancellation(models.Model):
    reason = models.CharField(max_length=255, null=False, blank=False, default="No reason given.")
    cancellation_date = models.DateField(null=False, blank=False, default=timezone.now)
    booking = models.ForeignKey(
        Booking,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        default=None
    )

    def __str__(self):
        return f"{self.booking.user.name} ({self.cancellation_date}) - ID:{self.id}"
    
    class Meta:
        verbose_name = "Cancellation"
        verbose_name_plural = "Cancellations"