"""

如何利用进程池
多进程库提供了Pool类来实现简单的多进程任务，Pool类有以下方法
apply() ： 直到得到结果之前一直阻塞
apply_async()：这是apply() 方法的一个变体，返回的是一个result对象，这是一个异步的操作
map() 这是内置的map() 函数的并行版本，在得到结果之前一直阻塞，此方法将可迭代的数据的每一个元素
作为进程的一个任务来执行

"""

import multiprocessing


def function_square(data):
    result = data * data
    return result


if __name__ == '__main__':
    inputs = list(range(100))
    pool = multiprocessing.Pool(processes=10)
    pool_outputs = pool.map(function_square, inputs)
    pool.close()
    pool.join()
    print('Pool:', pool_outputs)
