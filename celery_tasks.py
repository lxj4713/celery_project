from __future__ import absolute_import
from celery import chain
from celery_app import app
from utils import now_time
from task_work import start_work, async_work, end_work


@app.task()
def start_task(params):
    return start_work(now_time(), params)


@app.task()
def async_task(params):
    return async_work(now_time(), params)


@app.task()
def end_task(params):
    return end_work(now_time(), params)

