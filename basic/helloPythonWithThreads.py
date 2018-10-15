from threading import Thread
from time import sleep

# create the class inheriting Thread.
class CookBook(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.message = "Hello parallel python cookbook!\n"

	# this method prints the message
	def print_message(self):
		print(self.message)

	def run(self):
		print("Thread starting\n")
		x = 0 
		while(x < 10):
			self.print_message()
			sleep(2)
			x +=1
		print("Threading ended\n")


# start the main process
print("process started")

hello = CookBook()
hello.start()
print("Process ended")


# 主程序执行结束的时候，线程依然会每个两秒钟就打印一次信息，此例子证实线程是在父进程下执行的一个子任务
# 永远不要留下任何线程在后台默默运行，否则大型程序中将带给你无限痛苦。








