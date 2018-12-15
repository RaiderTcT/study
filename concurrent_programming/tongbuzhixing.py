# p.submit(task,i).result()即同步执行
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import os
import time
import random


def task(n):
    print('{} is running'.format(os.getpid()))
    time.sleep(2)
    return n**2


if __name__ == '__main__':
    p = ProcessPoolExecutor()
    start = time.time()
    for i in range(10):
        res = p.submit(task, i).result()
        print(res)
    # with ProcessPoolExecutor() as p:
    #     future_tasks = [p.submit(task, i) for i in range(10)]
    print('='*30)
    #print([obj.result() for obj in future_tasks])
    print(time.time()-start)
