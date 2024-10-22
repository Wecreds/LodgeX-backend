from django.db import models

class Promotion(models.Model):
    discount_percentage = models.IntegerField()
    expiration_date = models.DateField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description