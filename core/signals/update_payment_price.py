from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import BookingService, Payment

@receiver(post_save, sender=BookingService)
def update_payment_price(sender, instance, created, **kwargs):
        payment = Payment.objects.filter(booking=instance.booking).first()
        if payment:
            payment.save()