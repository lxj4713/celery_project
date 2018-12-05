import socket
from utils import now_time
from celery_tasks import start_task, async_task, end_task


# ip = '10.12.13'

def task_uuid():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip = s.getsockname()[0]
    # ip str = ip.replace('.','-')
    task_id = now_time() + '-' + ip + '-'
    return task_id


def start(tasks_name, params):
    task = None
    if tasks_name == 'start':
        task = start_task.apply_async(args=(params,), task_id=task_uuid() + tasks_name)
    elif tasks_name == 'async':
        task = async_task.apply_async(args=(params,), task_id=task_uuid() + tasks_name)
    elif tasks_name == 'end':
        task = end_task.apply_async(args=(params,), task_id=task_uuid() + tasks_name)

    print('middleware - - - -', task)
