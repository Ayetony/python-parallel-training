"""

每个gevent线程都有一个hub，hub是greenlet.greenlet的实例。hub实例在需要的时候创生（Lazy Created）
之后任何的Greenlet（注意是greenlet.greenlet的子类）实例的parent都设置成hub。
hub调用libev提供的事件循环来处理Greenlet代表的任务，当Greenlet实例结束（正常或者异常）之后，
执行逻辑又切换到hub。

每一个greenlet.greenlet实例都有一个parent（可指定，默认为创生新的greenlet.greenlet所在环境），
当greenlet.greenlet实例执行完逻辑正常结束、或者抛出异常结束时，执行逻辑切回到其parent。
可以继承greenlet.greenlet，子类需要实现run方法，当调用greenlet.switch方法时会调用到这个run方法

"""

import greenlet

import gevent


def callback(event, args):
    print(event, args[0], "---->", args[1])


def start():
    print('starting now')
    gevent.sleep(1)
    print('context goes back to start method')


def suspend():
    print('context goes to suspend method')
    gevent.sleep(1)
    print('context goes back to suspend method')


if __name__ == '__main__':
    print('main greenlet info.', greenlet.greenlet.getcurrent())
    print('hub info.', gevent.get_hub())
    trace = greenlet.settrace(callback)

    gevent.joinall([
        gevent.spawn(start),
        gevent.spawn(suspend)
    ])

    # gevent.spawn创建一个新的Greenlet，并注册到hub的loop上，调用gevent.joinall或者Greenlet.join的时候开始切换到hub。
    greenlet.settrace(trace)
