from __future__ import absolute_import

import os

import celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cbug.settings')

app = celery.Celery('cbug-cellar')

app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()

