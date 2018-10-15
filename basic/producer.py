from threading import Thread, Condition

condition = Condition()
items = []


class producer(Thread):

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
            time.sleep()
            self.pro
