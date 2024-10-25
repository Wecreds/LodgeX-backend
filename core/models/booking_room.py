from django.db import models
from core.models import Booking, Room

class BookingRoom(models.Model):
    room = models.ForeignKey(
        Room,
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
        return f"{self.room} - {self.booking.user.name}  ({self.booking.booking_date}) - ID:{self.id}"
    
    class Meta:
        verbose_name = "Booking Room"
        verbose_name_plural = "Bookings Rooms"