import logging

from cbug.celery import app as celery_app


@celery_app.task(bind=True, ignore_result=False)
def process_chunk(self, x):
    logging.error(" ~ executing process-chunk: %s" % x)
    return x * 2


@celery_app.task(bind=True, ignore_result=False)
def post_step_1(self, y):
    logging.error(" ~ executing post-step-1")
    return y * 3


@celery_app.task(bind=True, ignore_result=False)
def post_step_2(self, z):
    logging.error(" ~ executing post-step-2")
    return z * 5
