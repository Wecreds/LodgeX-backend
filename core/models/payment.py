from django.db import models
from core.models import Booking, BookingRoom, RoomAvailability, BookingService
from django.utils import timezone

class Payment(models.Model):
    class PaymentStatus(models.IntegerChoices):
        PENDING = 1, "PENDING"
        PAID = 2, "PAID"
    
    class PaymentMethod(models.IntegerChoices):
        CREDIT_CARD = 1, "CREDIT CARD"
        DEBIT_CARD = 2, "DEBIT CARD"
        CASH = 3, "CASH"
        PIX = 4, "PIX"

    payment_status = models.IntegerField(choices=PaymentStatus, default=PaymentStatus.PENDING, null=False, blank=False)
    booking_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0.0)
    service_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0.0)
    payment_date = models.DateField(null=True, blank=True)
    payment_method = models.IntegerField(choices=PaymentMethod, default=PaymentMethod.PIX, null=False, blank=False)
    booking = models.ForeignKey(
        Booking, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        default=None
    )

    def save(self, *args, **kwargs):
        if self.payment_status == self.PaymentStatus.PENDING:
            total_price = 0
            booking_rooms = BookingRoom.objects.filter(booking=self.booking)
            booking_availabilities = RoomAvailability.objects.filter(booking=self.booking)

            for booking_room in booking_rooms:
                for booking_availability in booking_availabilities:
                    if booking_availability.room == booking_room.room:
                        days_stayed = (booking_availability.end_date - booking_availability.start_date).days
                        room_price = booking_room.room.price_by_day * days_stayed
                        
                        guest_count = booking_availability.guest_count
                        room_total_price = room_price * guest_count  
                        total_price += room_total_price

            if self.booking.discount_coupon:
                discount = (total_price * self.booking.discount_coupon.discount_percentage) / 100
                total_price -= discount

            self.booking_price = total_price
        
        if BookingService.objects.filter(booking=self.booking).exists():
            booking_services = BookingService.objects.filter(booking=self.booking)
            self.service_price = 0
            for booking_service in booking_services:
                self.service_price += booking_service.service.price

        if self.payment_status == self.PaymentStatus.PAID and self.payment_date is None:
            self.payment_date = timezone.now().date()

        super(Payment, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.booking.user.name} ({self.booking.booking_date}) - Status: {self.get_payment_status_display()} - ID:{self.id}"
    
    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
