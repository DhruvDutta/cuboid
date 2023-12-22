from django.contrib.auth.models import User
from django.db import models
import uuid
from django.utils import timezone


class Employee(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='employee')
    token = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.user.username


class Box(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE)
    length = models.DecimalField(max_digits=5, decimal_places=2)
    breadth = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def area(self):
        return self.length * self.breadth

    @property
    def volume(self):
        return self.length * self.breadth * self.height

    def __str__(self):
        return self.employee.user.username + " "+str(self.created_at)+" "+str(self.updated_at)
