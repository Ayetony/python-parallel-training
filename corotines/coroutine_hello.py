import asyncio
import time
from random import randint


# practice finite state machine or automation,FSA

def start_state():
    print("Start called \n")
    input_value = randint(0, 1)
    time.sleep(1)
    if input_value == 0:
        result = yield from State2(input_value)
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
        result = yield from State2(input_value)
    result = "State 1 calling" + result
    return output_val + str(result)


@asyncio.coroutine
def State2(transition_value):
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
