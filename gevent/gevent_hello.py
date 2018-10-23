"""

to install the module gevent .

pip install setuptools cffi 'cython>=0.28' git+git://github.com/gevent/gevent.git#egg=gevent

the features of gevent

Fast event loop based on libev or libuv.   基于libev快速事件循环
Lightweight execution units based on greenlets. 基于greenlets的轻量级执行单元
API that re-uses concepts from the Python standard library (for examples there are events and queues).
Cooperative sockets with SSL support
Cooperative DNS queries performed through a threadpool, dnspython, or c-ares.
Monkey patching utility to get 3rd party modules to become cooperative
TCP/UDP/HTTP servers
Subprocess support (through gevent.subprocess)
Thread pools

"""

# 网络任务操作

import gevent
from gevent import socket

urls = ['www.baidu.com', 'www.example.com', 'www.python.org']
jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
gevent.joinall(jobs, timeout=3)
print([job.value for job in jobs])