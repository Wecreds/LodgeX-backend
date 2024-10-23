from django.db import models
from core.models import Booking, Service

class BookingService(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.DO_NOTHING,
        null=False,
        blank=False,
        default=None
    )
    booking = models.ForeignKey(
        Booking,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        default=None
    )

    def __str__(self):
        return f"{self.service} - {self.booking}"
    
    class Meta:
        verbose_name = "Booking Service"
        verbose_name_plural = "Bookings Services"