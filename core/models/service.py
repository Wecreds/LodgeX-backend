from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, default="No service name given.")
    price = models.DecimalField(default=0, decimal_places=2, max_digits=5, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False, default="No description given.")

    def __str__(self):
        return f"{self.name} - ID:{self.id}"
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"