from django.db import models
from core.models import Booking
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

    payment_status = models.IntegerField(choices=PaymentStatus, default=PaymentStatus.PENDING)
    payment_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0.0)
    payment_date = models.DateField(null=True, blank=True)
    payment_method = models.IntegerField(choices=PaymentMethod, default=PaymentMethod.PIX)
    booking = models.ForeignKey(
        Booking, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        default=None
    )

    def save(self, *args, **kwargs):
        if self.payment_status == self.PaymentStatus.PAID and self.payment_date is None:
            self.payment_date = timezone.now().date()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.booking} - {self.payment_date}({self.payment_status})"
    
    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"