import multiprocessing
import os
import random
import time
from threading import Thread


class Producer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        for item in range(1, 13):
            item = random.randint(1, 287)
            self.queue.put(item)
            print("Produce one item %s" % item)
            time.sleep(2)


class Consumer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        index = 0
        while True:
            item = self.queue.get()
            index += 1
            print("Consume one item %s" % str(item))
            print("index value : %s" % index)
            if index >= 13:
                os._exit(0)


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process_producer = Producer(queue)
    process_consumer = Consumer(queue)
    # process_producer.setDaemon(True)
    # process_consumer.setDaemon(True)
    process_producer.start()
    process_consumer.start()

    process_consumer.join()
    process_producer.join()
