from django.db import models
from core.models import Booking
from django.utils import timezone

class Cancellation(models.Model):
    reason = models.CharField(max_length=255, null=False, blank=False, default="Sem razão dada.")
    cancellation_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0.0)
    cancellation_date = models.DateField(null=False, blank=False, default=timezone.now().date())
    booking = models.ForeignKey(
        Booking,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        default=None
    )

    def __str__(self):
        return f"{self.booking} - {self.cancellation_date}"
    
    class Meta:
        verbose_name = "Cancellation"
        verbose_name_plural = "Cancellations"