# yourvenv/cfehome/celery.py
from __future__ import absolute_import, unicode_literals  # for python2
from celery.schedules import crontab
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
# this is also used in manage.py
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo_e_newspaper.settings')

## Get the base REDIS URL, default to redis' default
BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')

app = Celery('demo_e_newspaper')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.broker_url = BASE_REDIS_URL



# this allows you to schedule items in the Django admin.
# app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'



app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'newspaper.tasks.tasks.schedule_populate_news_data',
        'schedule': 30,
        # 'args': (),
    },
}
