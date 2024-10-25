from django.db import models
from core.models import Room

from uploader.models import Image

class RoomPhoto(models.Model):
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        default=None
    )
    photo = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        default=None,
    )

    def __str__(self):
        return f"{self.room} - {self.photo.description} - ID:{self.id}"
    
    class Meta:
        verbose_name = "Room Photo"
        verbose_name_plural = "Room Photos"