"""
python的多进程模块提供了在所有的用户间管理共享信息的管理者Manager，一个
管理者对象控制着所有python对象的服务进程，允许其他进程操作共享对象。

有如下特性：
    控制着管理共享对象的服务进程
    确保进程修改了共享对象之后，所有的进程拿到的共享对象是更新过的

"""

import multiprocessing


def worker(dictionary, key, item):
    dictionary[key] = item
    print("key = %d value = %d" % (key, item))


if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    dictionary = mgr.dict()
    jobs = [multiprocessing.Process(target=worker, args=(dictionary, i, i*2)) for i in range(10)]
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()

    print('results', dictionary)


























