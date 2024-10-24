from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, default="No category name given.")

    def __str__(self):
        return f"{self.name} - {self.id}"
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"