from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from django.utils import timezone
from .models import Box
from .validators import validate_total_boxes_weekly, validate_total_boxes_user_weekly, validate_average_area, validate_average_volume
import math


@receiver(pre_save, sender=Box)
def pre_save_box(sender, instance, **kwargs):
    boxes = Box.objects.all()
    area = instance.length*instance.width
    volume = instance.length*instance.width*instance.height
    average_area = (sum(box.area for box in boxes)+area) / \
        len(boxes) if len(boxes) > 0 else 0
    average_volume = (sum(box.volume for box in boxes) + volume) / \
        len(boxes) if len(boxes) > 0 else 0
    try:
        validate_average_area(average_area)
        validate_average_volume(average_volume)
    except Exception as e:
        # Raise a ValidationError to abort the save operation
        raise e


@receiver(pre_delete, sender=Box)
def pre_delete_box(sender, instance, **kwargs):
    boxes_weekly = Box.objects.filter(
        created_at__gte=timezone.now() - timezone.timedelta(days=7))
    total_boxes_weekly = boxes_weekly.count()

    validate_total_boxes_weekly(total_boxes_weekly)

    boxes_user_weekly = boxes_weekly.filter(owner=instance.owner)
    total_boxes_user_weekly = boxes_user_weekly.count()

    validate_total_boxes_user_weekly(total_boxes_user_weekly)
