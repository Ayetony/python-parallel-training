import multiprocessing
import time


def function_work():
    print('Starting function')
    time.sleep(0.1)
    print('Finished function')


if __name__ == '__main__':
    p = multiprocessing.Process(target=function_work)
    print('Process before execution :', p, p.is_alive())
    p.start()
    print('process running:', p, p.is_alive())
    p.terminate()
    print('process terminated:', p, p.is_alive())
    p.join()
    print('Process joined ', p, p.is_alive())
    print('Process exit code:', p.exitcode)
