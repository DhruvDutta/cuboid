from django.db import models
from django.contrib.auth.models import User
import uuid


class Box(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    length = models.DecimalField(max_digits=5, decimal_places=2)
    breadth = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    area = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    volume = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        # Automatically set 'area' when saving the model
        self.area = self.length * self.breadth
        self.volume = self.length * self.breadth * self.height
        super().save(*args, **kwargs)
