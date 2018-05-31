# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import string

import celery
from django.utils.crypto import get_random_string

from rest_framework.response import Response
from rest_framework.views import APIView

from cbug.apps.api import tasks


class StartView(APIView):
    def get(self, request):
        chord_key = get_random_string(6, string.ascii_lowercase)
        all_tasks = celery.chord(
            task_id="chord-%s" % chord_key,
            header=celery.group(
                tasks.process_chunk.subtask(args=(x,), task_id="chord-%s-chunk-%s-%s" % (chord_key, i, x))
                for i, x in enumerate(range(10, 15))
            ),
            # immutable = ignore results from parent
            body=celery.chain(
                tasks.post_step_1.subtask(args=(20,), task_id="chord-%s-post-1" % chord_key, immutable=True),
                tasks.post_step_2.subtask(args=(20,), task_id="chord-%s-post-1" % chord_key, immutable=True),
            )
        )
        result = all_tasks.apply_async()
        return Response(data=dict(chord_key=chord_key, result=repr(result)))
