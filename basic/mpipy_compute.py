"""
python 提供了很多MPI模块写并行程序，其中mpi4py是一个紧跟C++绑定的MPI-2
主要应用有：点对点通讯，集体通讯，拓扑
"""

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print('hello world from process', rank)

if rank == 1:
    destination_process = 8
    data = 'hello'
    comm.send(data, dest=destination_process)
    print("sending data %s :" % data + "to process %d" % destination_process)

if rank == 4:
    data = comm.recv(source=0)
    print("data received is = %s" % data)

if rank == 8:
    data1 = comm.recv(source=1)
    print('data1 receives is = % s' % data1)
