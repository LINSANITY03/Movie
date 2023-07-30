from __future__ import absolute_import, unicode_literals
from celery import Celery

from django.conf import settings

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Movies.settings')

app = Celery('Movies')
app.config_from_object(settings, namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
