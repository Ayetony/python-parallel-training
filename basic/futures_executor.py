"""

线程池和进程池是用于优化和简化线程或者进程的使用。
通过池提交任务给executor
池由两部分组成，一个是内部的队列，存放着执行的任务，另一部分是一些列的进程或者线程，用于执行
这些任务。池的的主要目的是为了重用。

"""
import concurrent.futures
import time

number_list = [1, 2, 3, 4, 5, 6, 7, 7, 9]


def evaluate_item(x):
    result_item = count(x)
    return result_item


def count(number):
    for i in range(0, 10000000):
        i = i + 1
    return i + number


if __name__ == '__main__':
    start_time = time.time()
    for item in number_list:
        print(evaluate_item(item))
    print('Sequential execution in' + str(time.time() - start_time), 'seconds')

    start_time_two = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(evaluate_item, item) for item in number_list]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())
    print('Thread pool execution in' + str(time.time() - start_time_two), "seconds")

    start_time_three = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(evaluate_item, item) for item in number_list]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())
    print('Process pool execution in ' + str(time.time() - start_time_three), 'seconds')



