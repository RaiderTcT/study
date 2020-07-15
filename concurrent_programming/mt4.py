"""
同步原语：锁

"""
import threading, multiprocessing
import time
import random

lock = threading.Lock()
# ThreadLocal对象，每个Thread对它都可以读写type属性，但互不影响
# 虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰
local_tmp = threading.local()
number = 0
def plus():
    global number
    for i in range(1000000):
        number += 1
    print(f"{threading.current_thread().name} result:{number}")
    
def plus_lock():
    global number
    with lock:
        for i in range(1000000):
            number += 1
    print(f"{threading.current_thread().name} result:{number}")

def main():
    print(f"函数起始时间1：{time.ctime()}")
    for i in range(3):
        t = threading.Thread(target=plus_lock, name='plus_{}'.format(i))
        t.start()
    time.sleep(2)
    print(f"函数结束时间1：{time.ctime()}\n number:{number}")


if __name__ == "__main__":
    main()
    # print(multiprocessing.cpu_count())