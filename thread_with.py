import threading
import logging
logging.basicConfig(level='DEBUG')


def threading_with(statement):
    with statement:
        logging.debug('acquired via with,the thread name is ' + str(statement) +
                      str(threading.current_thread().getName()))


def threading_not_with(statement):
    statement.acquire()
    try:
        logging.debug('acquired ,threadname is' + str(statement) + str(threading.current_thread().getName()))
    finally:
        statement.release()


if __name__ == '__main__':
    # test battery
    lock = threading.Lock()
    rlock = threading.RLock()
    condition = threading.Condition()
    mutex = threading.Semaphore(1)

    threading_synchronization_list = [lock, rlock, condition, mutex]
    for statement in threading_synchronization_list:
        t1 = threading.Thread(target=threading_with, args=(statement,))
        t2 = threading.Thread(target=threading_not_with, args=(statement,))

        t1.start()
        t2.start()
        t1.join()
        t2.join()







