from kombu import Exchange, Queue

# broker='redis://:12345678@192.168.110.130:63800/'
# backend='redis://:12345678@192.168.110.130:6380/'
BROKER_URL = 'redis://@127.0.0.1:6379/1'
CELERY_RESULT_BACKEND = 'redis://@127.0.0.1:6379/2'
CELERY_QUEUES = (
    # Queue("default", Exchange("default"), routing_key="default"),
    Queue("at", Exchange("at"), routing_key="at"),
    Queue("bt", Exchange("bt"), routing_key="bt"),
    Queue("ct", Exchange("ct"), routing_key="ct"),
)

CELERY_ROUTES = {
    'celery_tasks.start_task': {"queue": "at", "routing_key": "at"},
    'celery_tasks.async_task': {"queue": "bt", "routing_key": "bt"},
    'celery_tasks.end_task': {"queue": "ct", "routing_key": "ct"},
}

CELERYD_CONCURRENCY = 2

# from celery.schedules import crontab
# imports =[
#     ''
# ]

# from celery.schedules import crontab
# from .celery_pro import celery_pro
#
# celery_pro.conf.update(
#     CELERYBEAT_SCHEDULE = {
#         'sum-task': {
#             'task': 'deploy.tasks.add',
#             'schedule':  timedelta(seconds=20),
#             'args': (5, 6)
#         },
#         'send-report': {
#             'task': 'deploy.tasks.report',
#             'schedule': crontab(hour=4, minute=30, day_of_week=1),
#         }
#     }
# )


# from celery import platforms
#
# platforms.C_FORCE_ROOT = True
