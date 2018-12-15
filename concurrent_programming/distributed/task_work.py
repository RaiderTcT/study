import multiprocessing
from multiprocessing.managers import BaseManager
import sys
import time
import queue


class QueueManager(BaseManager):
    pass


if __name__ == "__main__":
    # 注册函数调用服务器
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')
    # 连接到服务器
    server_addr = '127.0.0.1'
    print('Try to connnect to server %s\n' % server_addr)
    manager = QueueManager(address=(server_addr, 5000), authkey=b'123456')
    # 从网络连接
    manager.connect()
    # 获取queue
    result = manager.get_result_queue()
    task = manager.get_task_queue()
    # 从task_queue 获取任务,放入result_queue
    for i in range(100):
        try:
            n = task.get(timeout=1)
            print('get data: %s\n' % n)
            r = n**2
            print('calcute %s * %s\n' % (n, n))
            time.sleep(0.5)
            result.put(r)
        except queue.Empty:
            print('all work have been done')
    print('exit')
