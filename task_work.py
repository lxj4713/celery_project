import time
from utils import now_time


def start_work(times, params):
    time.sleep(5)
    # return 'work - 1'
    return ([{params:'start'},{times:now_time()}])


def async_work(times, params):
    time.sleep(10)
    return ([{params: 'async'}, {times: now_time()}])


def end_work(times, params):
    time.sleep(15)
    return ([{params: 'end'}, {times: now_time()}])
