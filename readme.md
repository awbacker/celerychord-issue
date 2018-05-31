# Redis pub-sub channels not released

## Running

### Requirements

* `pipenv`
* `redis 3.0.9` accessible at localhost:6379

##  Running

Open 3 terminals.  In the first, start the API server.  In the second start
the celery worker.  The 3rd terminal will be used to kick off the request and
show the channels.

Relevant Files Are:

* [tasks.py](cbug/apps/api/tasks.py)
* [views.py](cbug/apps/api/views.py)

**Terminal 1**

    $> pipenv shell
    $> ./manage.py runserver

**Terminal 2**

    $> pipenv shell
    $> celery worker -A cbug
    ...
    [config]
    .> app:         cbug-cellar:0x107f7ad10
    .> transport:   redis://localhost:6379/1
    .> results:     redis://localhost:6379/1
    .> concurrency: 1 (prefork)
    .> task events: OFF (enable -E to monitor tasks in this worker)


**Terminal 3**

    $> pipenv shell
    $> redis-cli pubsub channels
    (empty list)

Start the request:

    $> http :8000/api/start/
    # (-or- curl localhost:8000/api/start/)
    HTTP/1.0 200 OK
    {
        "chord_key": "lphsmq",
        "result": "<AsyncResult: chord-lphsmq-post-1>"
    }

Check out the channels again.  Each hit to the `/api/start/` endpoint will
leave 5 more tasks open (with a different chrod id)

    $> redis-cli pubsub channels
    1) "celery-task-meta-chord-lphsmq-chunk-4-14"
    2) "celery-task-meta-chord-lphsmq-chunk-2-12"
    3) "celery-task-meta-chord-lphsmq-chunk-3-13"
    4) "celery-task-meta-chord-lphsmq-chunk-1-11"
    5) "celery-task-meta-chord-lphsmq-chunk-0-10"


