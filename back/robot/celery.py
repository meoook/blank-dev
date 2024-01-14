import os
from celery import Celery
from celery.schedules import crontab
# from core.tasks import check_all_file_repos

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'robot.settings')
app = Celery('robot')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# app.conf.update(
#     task_serializer='json',
#     accept_content=['json'],  # Ignore other content
#     result_serializer='json',
#     timezone='Europe/Oslo',
#     enable_utc=True,
# )


# Scheduled task here
app.conf.beat_schedule = {
    'files-update-from-repo': {
        'task': 'check_all_file_repos',
        'schedule': crontab(minute=0, hour='*/2'),
    },
    'copy-refresh-then-to-repo': {
        'task': 'refresh_copies',
        'schedule': crontab(minute=0, hour='1,3,5,7,9,11,13,15,17,19,21,23'),
    },
}

