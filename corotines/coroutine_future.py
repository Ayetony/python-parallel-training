import asyncio
import sys

"""
Asyncio下的模块Futures，是定制化的，就是还有多少未完成的事。

cancel() 取消future的执行，调度回调函数
result() 返回future代表的结果
exception() 返回future中的exception
add_done_callback(fn) 从call when done列表中移除callback实例
set_result(result) 将future标注为执行完成，设置result值
set——exception() 执行完成，设置Exception


"""


@asyncio.coroutine
def future_coroutine(future, N):
    count = 0
    for i in range(1, N + 1):
        count += 1
    yield from asyncio.sleep(4)
    future.set_result("first coroutine (Sum of N integers) result is :" + str(count))


@asyncio.coroutine
def second_coroutine(future, N):
    count = 1
    for i in range(2, N + 1):
        count *= i
    yield from asyncio.sleep(3)
    future.set_result("second coroutine (factorial) result = " + str(count))


def got_result(future):
    print(future.result())


if __name__ == '__main__':
    N1 = int(sys.argv[1])
    N2 = int(sys.argv[2])
    loop = asyncio.get_event_loop()
    future_one = asyncio.Future()
    future_two = asyncio.Future()
    tasks = [
        future_coroutine(future_one, N1),
        second_coroutine(future_two, N2)
    ]
    future_one.add_done_callback(got_result)
    future_two.add_done_callback(got_result)
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
