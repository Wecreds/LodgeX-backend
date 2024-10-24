from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

from core.models import Booking, User

class Feedback(models.Model):
    class FeedbackStatus(models.IntegerChoices):
        PENDING = 1, "PENDING"
        DECLINED = 2, "DECLINED"
        APPROVED = 3, "APPROVED"
    
    review_status = models.IntegerField(null=False, blank=False, choices=FeedbackStatus, default=FeedbackStatus.PENDING)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=False, blank=False, default=1, validators= [MinValueValidator(1), MaxValueValidator(5)])
    comment = models.CharField(null=False, blank=False, max_length=255, default="No comment given.")
    feedback_date = models.DateField(null=False, blank=False, default=timezone.now)
    booking = models.ForeignKey(
        Booking, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        default=None
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        default=None
    )

    def __str__(self):
        return f"{self.user.name} ({self.feedback_date}) - Review: {self.get_review_status_display()}"
    
    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"