import multiprocessing
from multiprocessing.managers import BaseManager
import random
import time
import queue

task_queue = queue.Queue()
result_queue = queue.Queue()


def return_task():  # 返回任务队列
    return task_queue


def return_result():  # 返回结果队列
    return result_queue


class QueueManager(BaseManager):  # 进程管理共享数据
    pass


if __name__ == "__main__":

    multiprocessing.freeze_support()  # 开启分布式支持
    QueueManager.register('get_task_queue', callable=return_task)
    QueueManager.register('get_result_queue', callable=return_result)
    # 创建一个管理器，设置地址与密码
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'123456')
    manager.start()
    task, result = manager.get_task_queue(), manager.get_result_queue()
    # 添加任务
    for i in range(100):
        r = random.randint(1, 1000)
        print('task add data: %s\n' % r)
        task.put(r)
    dis = '-' * 20
    print('waiting for %s' % dis)
    # 读取结果
    for i in range(100):
        res = result.get(timeout=100)
        print('get data:%s\n' % res)
    manager.shutdown()
    print('server close')