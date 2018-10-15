import threading
import time


class Box(object):
    lock = threading.RLock()

    def __init__(self):
        self.total_items = 0

    def execute(self, n):
        Box.lock.acquire()
        self.total_items += n
        Box.lock.release()

    def add(self):
        Box.lock.acquire()
        self.execute(1)
        Box.lock.release()

    def remove(self):
        Box.lock.acquire()
        self.execute(-1)
        Box.lock.release()

# run these threads separately


def adder(box, item):
    while item > 0:
        print("Adding 1 item in the box")
        box.add()
        time.sleep(1)
        item -= 1


def remover(box, item):
    while item > 0:
        print("removing 1 item in the box")
        box.remove()
        time.sleep(1)
        item -= 1


if __name__ == "__main__":
    items = 5
    print("putting %s items in the box" % items)
    boxOne = Box()

    t1 = threading.Thread(target=adder, args=(boxOne, items))
    t2 = threading.Thread(target=remover, args=(boxOne, items))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("The final value of item %s" % boxOne.total_items)




