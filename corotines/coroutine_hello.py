import asyncio
import time
from random import randint

"""
asyncio 是用来处理事件循环中的异步进程和并发任务执行的，它还提供了 asyncio.Task() 可以
在任务中使用协程，它的作用是在同一事件循环中，运行其一个任务的同时可以并发底运行多个任务。
当协程被包在任务中，它会自动将任务和事件循环连接起来，事件启动，任务自动运行。这样提供了一个
可以自动驱动协程的机制。

"""


# practice finite state machine or automation,FSA

def start_state():
    print("Start called \n")
    input_value = randint(0, 1)
    time.sleep(1)
    if input_value == 0:
        result = yield from state2(input_value)
    else:
        result = yield from state1(input_value)

    print("Resume of the translation: \n Start state calling" + result)


@asyncio.coroutine
def state1(transition_value):
    output_val = str("State 1 with transition value = %s \n" % transition_value)
    input_value = randint(0, 1)
    time.sleep(1)
    print("...Evaluating ..")
    if input_value == 0:
        result = yield from state3(input_value)
    else:
        result = yield from state2(input_value)
    result = "State 1 calling" + result
    return output_val + str(result)


@asyncio.coroutine
def state2(transition_value):
    output_val = str("State 2 with transition value = %s \n" % transition_value)
    input_value = randint(0, 1)
    time.sleep(1)
    print("... Evaluating...")
    if input_value == 0:
        result = yield from state1(input_value)
    else:
        result = yield from state3(input_value)

    result = "State 2 calling " + result
    return output_val + str(result)


@asyncio.coroutine
def state3(transition_value):
    output_val = str("State 3 with transition value = %s \n" % transition_value)
    input_value = randint(0, 1)
    time.sleep(1)
    print("...Evaluating ...")
    if input_value == 0:
        result = yield from state1(input_value)
    else:
        result = yield from end_state(input_value)
    result = "State 3 calling" + result
    return output_val + str(result)


@asyncio.coroutine
def end_state(transition_value):
    output_val = str("End state with transition value =%s \n" % transition_value)
    print("... Stop Computation")
    return output_val


if __name__ == "__main__":
    print("Finite state machine simulation with asyncio coroutine")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_state())
