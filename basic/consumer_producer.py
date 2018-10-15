import time
from threading import Thread, Condition

items = []
condition = Condition()

"""
  Condition() instance 
  
  method ,condition.acquire - fetch the resource 
  condition.wait()  jsut hold on ,wait
  condition.notify() notify other threads.
  condition.release() , let it go, you are finished.

"""


class Consumer(Thread):

    def __init__(self):
        Thread.__init__(self)

    def consume(self):
        global condition
        global items
        condition.acquire()
        if len(items) == 0:
            condition.wait()
            print("Consumer notify: no items to consume")
        items.pop()
        print("Consumer notify: consumed 1")
        print("Consumer notify: items to consume are %s" % len(items))

        condition.notify()
        condition.release()

    def run(self):
        for i in range(0, 30):
            time.sleep(2)
            self.consume()


class Producer(Thread):

    def __init__(self):
        Thread.__init__(self)

    def produce(self):
        global condition
        global items
        condition.acquire()
        if len(items) == 10:
            condition.wait()
            print("Producer notify: items produced are %s" % len(items))
            print("Producer notify: stop the production")

        items.append(1)
        print("Producer notify: total items produced are %s" % len(items))
        condition.notify()
        condition.release()

    def run(self):
        for i in range(0, 20):
            time.sleep(2)
            self.produce()


if __name__ == '__main__':

    consumer = Consumer()
    producer = Producer()

    consumer.start()
    producer.start()

    producer.join()
    consumer.join()




