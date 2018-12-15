"""
BoundedSemaphore。这种锁允许一定数量的线程同时更改数据，它不是互斥锁。
比如地铁安检，排队人很多，工作人员只允许一定数量的人进入安检区，其它的人继续排队。
"""
import threading
import time

maxconnections = 5
# ...
pool_sema = threading.BoundedSemaphore(value=maxconnections)


def run(n):
    with pool_sema:
        print(f'run thread {n}')
        time.sleep(1)


# 运行结果是 5个 一批 分批来的
for i in range(20):
    t = threading.Thread(target=run, args=(i,))
    t.start()
