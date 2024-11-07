from django.db import models

from uploader.models import Image

class LodgePhoto(models.Model):
    photo = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        default=None,
    )

    def __str__(self):
        return f"{self.photo.description} - ID:{self.id}"
    
    class Meta:
        verbose_name = "Lodge Photo"
        verbose_name_plural = "Lodge Photos"