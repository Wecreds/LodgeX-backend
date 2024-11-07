from django.db import models
from core.models import DiscountCoupon, User
from django.utils import timezone

class Booking(models.Model):
    class BookingStatus(models.IntegerChoices):
        ACTIVE = 1, "ACTIVE"
        CANCELED = 2, "CANCELED"
        COMPLETED = 3, "COMPLETED"

    booking_status = models.IntegerField(choices=BookingStatus, default=BookingStatus.ACTIVE, null=True, blank=True)
    booking_date = models.DateField(default=timezone.now, null=False, blank=False)
    discount_coupon = models.ForeignKey(
        DiscountCoupon, 
        on_delete=models.PROTECT, 
        null=True, 
        blank=True, 
        default=None
    )
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        default=None
    )

    def __str__(self):
        return f"{self.user.name} ({self.booking_date}) - ({self.get_booking_status_display()}) - ID:{self.id}"
    
    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"