"""
Python 有个asynio模块，提供管理事件协程任务和线程的函数，以及编写并发代码的原语。此模块
的主要组建和概念如下。
事件循环：在asyncio模块中，每一个进程都有一个事件循环
协程：这是子程序的泛化概念，可以在执行期间暂停，这样可以等待外部的处理完成之后，从之前暂停的
地方恢复执行。
futures：定义了Future对象,和concurrent.futures模块一样，表示尚未完成的计算
tasks:这是asyncio的子类，封装和管理并行模式下的协程。
"""

import asyncio


def function_run1(end_time, loop):
    print("function_run1 called")
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, function_run2, end_time, loop)
    else:
        loop.stop()


def function_run2(end_time, loop):
    print('function_run2 called')
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, function_run3, end_time, loop)
    else:
        loop.stop()


def function_run3(end_time, loop):
    print('function_run3 called')
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, function_run3, end_time, loop)
    else:
        loop.stop()


loop = asyncio.get_event_loop()
end_loop = loop.time() + 9.0
loop.call_soon(function_run1, end_loop, loop)
loop.run_forever()
loop.close()
