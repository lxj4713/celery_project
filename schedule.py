# from celery import chain
#
# from celery_tasks import first_task,second_task,third_task,fourth_task
#
#
# class TotalTask(object):
#     def __init__(self,name,action,params):
#         self.id = id
#         self.name = name
#         self.action = action
#         self.params = params
#
#     def step(self):
#         if self.name == 'bk':
#             cha = chain(first_task.s({'message':'OK'},self.action['first']) | second_task.s() | third_task.s())
#         else:
#             cha = chain(first_task.s(self.params) | fourth_task.s())
#         task_id = []
#         return {'info':'','id':task_id}
