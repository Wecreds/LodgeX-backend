from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=5)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name