from django.contrib import admin
from .models import Box, Employee
# Register your models here.
admin.site.register([Employee, Box])
