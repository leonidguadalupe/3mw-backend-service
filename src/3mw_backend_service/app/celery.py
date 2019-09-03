import os
from celery import Celery
from celery.schedules import crontab
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '3mw_backend_service.app.settings')

app = Celery('app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
