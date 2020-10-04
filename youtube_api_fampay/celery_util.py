import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youtube_api_fampay.settings')


celery_app = Celery("youtube_api_fampay")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")



# this cronjob will run every 3 minutes
celery_app.conf.beat_schedule = {
    'task': {
        'task': 'backend.tasks.fetch_latest_youtube_videos',
        'schedule': crontab(minute="*/1"),
    },
}
celery_app.autodiscover_tasks()