import threading
import time

def first_function():
	print(threading.currentThread().getName() + str('is starting'))
	time.sleep(2)
	print(threading.currentThread().getName() + str(' is Existing'))
	return 

def second_function():
	print(threading.currentThread().getName() + str('is starting'))
	time.sleep(2)
	print(threading.currentThread().getName() + str(' is Existing'))
	return 

def third_function():
	print(threading.currentThread().getName() + str('is starting'))
	time.sleep(2)
	print(threading.currentThread().getName() + str(' is Existing'))
	return 

# name can be given by the os or manual
if __name__ == '__main__':
	t1 = threading.Thread(name='first_function', target=first_function)
	t2 = threading.Thread(name='second_function', target=second_function)
	t3 = threading.Thread(target=third_function)

	t1.start()
	t2.start()
	t3.start()

	t1.join()
	t2.join()
	t3.join()
	

