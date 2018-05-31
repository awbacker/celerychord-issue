from __future__ import absolute_import, print_function, unicode_literals

from datetime import timedelta

CELERY_WORKER_CONCURRENCY = 1
CELERY_ENABLE_UTC = True
CELERY_TIMEZONE = 'UTC'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_BROKER_URL = 'redis://localhost:6379/1'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'
CELERY_TASK_DEFAULT_QUEUE = 'cbug-queue'
CELERY_RESULT_EXPIRES = timedelta(days=14)
CELERY_WORKER_PREFETCH_MULTIPLIER = 1
