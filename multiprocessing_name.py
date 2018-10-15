import multiprocessing
import time


def thread_name():
    name = multiprocessing.current_process().name
    print('starting %s\n' % name)
    time.sleep(3)
    print('Existing %s \n' % name)


if __name__ == '__main__':
    process_with_name = multiprocessing.Process(target=thread_name, name='foo_process')
    process_with_name.daemon = False  # run in background
    process_with_default_name = multiprocessing.Process(target=thread_name)

    process_with_name.start()
    process_with_default_name.start()

