"""

Queue thread design.

Methods:put(), get(), task_done().

join() to block.

"""

import random
import time
from threading import Thread
from queue import Queue


class Producer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(10):
            item = random.randint(0, 255)
            self.queue.put(item)
            print('Producer notify : item N %d appended to queue by %s' % (item, self.name))
            time.sleep(1)


class Consumer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            print('Consumer notify: item N %d out of the queue by name %s' % (item, self.name))
            self.queue.task_done()


if __name__ == '__main__':
    queue = Queue()
    producer = Producer(queue)
    consumer = Consumer(queue)

    producer.start()
    consumer.start()
    producer.join()
    consumer.run()


