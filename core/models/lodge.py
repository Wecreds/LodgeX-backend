from django.db import models

from uploader.models import Image


class Lodge(models.Model):
    lodge_name = models.CharField(max_length=100)
    lodge_location = models.TextField()
    lodge_description = models.TextField()
    lodge_landlord = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.lodge_name} - {self.lodge_location}"
    
    class Meta:
        verbose_name = "Lodge"
        verbose_name_plural = "Lodges"

class LodgeAmenity(models.Model):
    lodge = models.ForeignKey(Lodge, related_name="amenities", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.lodge.lodge_name}"

    class Meta:
        verbose_name = "Lodge Amenity"
        verbose_name_plural = "Lodge Amenities"

class LodgePolicy(models.Model):
    lodge = models.ForeignKey(Lodge, related_name="policies", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} - {self.lodge.lodge_name}"

    class Meta:
        verbose_name = "Lodge Policy"
        verbose_name_plural = "Lodge Policies"

class LodgePaymentMethod(models.Model):
    lodge = models.ForeignKey(Lodge, related_name="payment_methods", on_delete=models.CASCADE)
    method = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.method} - {self.lodge.lodge_name}"

    class Meta:
        verbose_name = "Lodge Payment Method"
        verbose_name_plural = "Lodge Payment Methods"

class LodgePhoto(models.Model):
    lodge = models.ForeignKey(Lodge, related_name="lodge_photos", on_delete=models.CASCADE)
    photo = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        default=None,
    )

    def __str__(self):
        return f"{self.photo.description} - ID:{self.lodge.lodge_name}"
    
    class Meta:
        verbose_name = "Lodge Photo"
        verbose_name_plural = "Lodge Photos"