"""
进程间共享数据
"""
from multiprocessing import Process, Array, Value

def f(v, a):
    v.value = 3.1415926
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    value = Value('d', 0.0) #
    array = Array('i', range(10)) # 数组类

    p = Process(target=f, args=(value, array))
    p.start()
    p.join()

    print(value.value)
    print(array[:])