"""
celery提供了下面的方法调用任务：
apply_async(args[,kwargs[,...]]) send a task message
delay(*args, **kwargs) send the task message in a quick way,but donot support that config the execution info

"""

from celery import Celery

app = Celery('addTask', broker='amqp://guest@localhost//')


@app.task
def add(x, y):
    return x+y


