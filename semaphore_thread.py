"""Using a Semaphore to synchronize threads"""

import threading
import time
import random

semaphore = threading.Semaphore(0)


def consumer():
    global item
    print("consumer is waiting ")
    semaphore.acquire()  # fetch the resource
    print("Consumer notify: consumed item number %s" % item)


def producer():
    global item
    time.sleep(10)
    # create a random item
    item = random.randint(0, 1000)
    print("Producer notify: produced item number %s" % item)
    semaphore.release()  # release the resource


if __name__ == '__main__':
    for i in range(0, 5):
        t1 = threading.Thread(target=producer)
        t2 = threading.Thread(target=consumer)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print("program terminated")


