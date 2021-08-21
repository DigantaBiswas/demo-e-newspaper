from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery import app
from django.contrib.auth.models import User


from demo_e_newspaper.celery import app


@shared_task()
def schedule_populate_news_data():
   print("working")
