from django.db import models
from django.core.validators import MinValueValidator

from core.models import Booking, Room

class RoomAvailability(models.Model):
    class RoomStatus(models.IntegerChoices):
        RESERVED = 1, "RESERVED"
        MAINTENANCE = 2, "MAINTENANCE"

    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    room_status = models.IntegerField(choices=RoomStatus, default=RoomStatus.RESERVED, null=False, blank=False)
    reason = models.CharField(max_length=200, null=True, blank=True)
    guest_count = models.IntegerField(default=1, validators= [MinValueValidator(1)])
    booking = models.ForeignKey(
        Booking, 
        on_delete=models.DO_NOTHING, 
        null=True, 
        blank=True, 
        default=None
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        default=None
    )

    def __str__(self):
        return f"{self.booking.user.name} {self.room.name} - {self.start_date} until {self.end_date} - ID:{self.id}"
    
    class Meta:
        verbose_name = "Room Availability"
        verbose_name_plural = "Room Availability"