from django.conf import settings
from django.core.exceptions import ValidationError


def validate_average_area(value):
    if value > settings.A1:
        raise ValidationError(
            f'The average area cannot exceed {settings.A1}.')


def validate_average_volume(value):
    if value > settings.V1:
        raise ValidationError(
            f'The average volume cannot exceed {settings.V1}.')


def validate_total_boxes_weekly(value):
    if value > settings.L1:
        raise ValidationError(
            f'The total boxes added in a week cannot exceed {settings.L1}.')


def validate_total_boxes_user_weekly(value):
    if value > settings.L2:
        raise ValidationError(
            f'The total boxes added in a week by a user cannot exceed {settings.L2}.')
