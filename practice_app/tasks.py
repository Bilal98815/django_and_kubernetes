from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import PracticeModel


@shared_task
def clear_table():
    cutoff_time = timezone.now() - timedelta(minutes=4)
    entries_to_delete = PracticeModel.objects.filter(created_at__lte=cutoff_time)
    num_deleted, _ = entries_to_delete.delete()
    return f"Deleted {num_deleted} entries older than 4 minutes"
