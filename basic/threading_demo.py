# 线程在进程内产生，线程之间共享内存，而进程之间是相互独立的
import threading

def function(i):
	print("function called by thread %i" % i)
	return 

threads = [] 

for i in range(5):
	t = threading.Thread(target=function, args=(i,))
	threads.append(t)
	t.start()
	t.join()

# pass


