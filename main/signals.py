from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from django.utils import timezone
from .models import Box
from .validators import validate_total_boxes_weekly, validate_total_boxes_user_weekly, validate_average_area, validate_average_volume


@receiver(pre_save, sender=Box)
def pre_save_box(sender, instance, **kwargs):
    boxes = Box.objects.all()
    average_area = sum(box.area for box in boxes) / \
        len(boxes) if len(boxes) > 0 else 0
    average_volume = sum(box.volume for box in boxes) / \
        len(boxes) if len(boxes) > 0 else 0

    validate_average_area(average_area)
    validate_average_volume(average_volume)


@receiver(pre_delete, sender=Box)
def pre_delete_box(sender, instance, **kwargs):
    boxes_weekly = Box.objects.filter(
        created_at__gte=timezone.now() - timezone.timedelta(days=7))
    total_boxes_weekly = boxes_weekly.count()

    validate_total_boxes_weekly(total_boxes_weekly)

    boxes_user_weekly = boxes_weekly.filter(owner=instance.owner)
    total_boxes_user_weekly = boxes_user_weekly.count()

    validate_total_boxes_user_weekly(total_boxes_user_weekly)
