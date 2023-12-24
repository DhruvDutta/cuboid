from django.conf import settings
from rest_framework.exceptions import ValidationError


def validate_average_area(value):
    if value > settings.A1:
        raise ValidationError(
            f'Average area must not excees {settings.A1}.')


def validate_average_volume(value):
    if value > settings.V1:
        raise ValidationError(
            f'Average volume must not excees {settings.V1}.')


def validate_total_boxes_weekly(value):
    if value > settings.L1:
        raise ValidationError(
            f'The total boxes added in this week cannot exceed {settings.L1}.')


def validate_total_boxes_user_weekly(value):
    if value > settings.L2:
        raise ValidationError(
            f'The total boxes added by you in this week cannot exceed {settings.L2}.')
