from django.db import models
from django.contrib.auth.models import User
from .validators import validate_average_area, validate_average_volume
from django.conf import settings
from django.http import JsonResponse


class Box(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    length = models.DecimalField(max_digits=5, decimal_places=2)
    width = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    area = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, validators=[validate_average_area])
    volume = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, validators=[validate_average_volume,])

    def save(self, *args, **kwargs):
        self.area = self.length * self.width
        self.volume = self.length * self.width * self.height

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.id) + " "+self.owner.username
