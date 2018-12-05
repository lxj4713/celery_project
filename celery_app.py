from __future__ import absolute_import  #拒绝隐式引入

from celery import Celery
# from celery_config import celery_config
# import config

app = Celery('celery_app',include=['celery_tasks'])

app.config_from_object('celery_config')
# broker=celery_config.BROKER_URL,
#     backend=celery_config.CELERY_RESULT_BACKEND,
#     CELERY_QUEUES = celery_config.CELERY_QUEUES,
#     CELERY_ROUTES = celery_config.CELERY_ROUTES,

# class CeleryConfig(object):
#     pass
#
# celery_pro = Celery(
#     'celery_tasks',
# )
#
# celery_pro.config_from_object(CeleryConfig)
# celery_pro.autodiscover_tasks()   #4.1可以不传参数


# celery_pro.conf.enable_utc = False
# celery_pro.conf.timezone = 'Asia/Shanghai'

# if __name__ == '__main__':
#     app.start()