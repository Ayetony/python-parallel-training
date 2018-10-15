import multiprocessing


class MyProcess(multiprocessing.Process):
    def run(self):
        print('called run method in process : %s' % self.name)
        return


if __name__ == '__main__':
    jobs = []
    for i in range(10):
        p = MyProcess()
        jobs.append(p)
        p.start()
        p.join()