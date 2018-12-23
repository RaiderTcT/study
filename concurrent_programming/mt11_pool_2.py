"""
一个基于thread和queue的线程池，以任务为队列元素，动态创建线程，
重复利用线程，通过close和terminate方法关闭线程池。
"""

import threading
import queue
import contextlib
import time

# 空对象， 停止线程
StopEvent = object()


def callback(status, result):
    """
    根据需要进行的回调函数，默认不执行。
    :param status: action函数的执行状态
    :param result: action函数的返回值
    :return:
    """
    pass


def action(thread_name, args):
    """
    真实的任务定义
    ：param thread_name: 执行该方法的线程名
    :param args: 该函数的参数
    """
    time.sleep(0.2)
    print(f"第{args+1}个任务调用线程{thread_name}！")


class ThreadPool:

    def __init__(self, max_num, max_task_num=None):
        """
        初始化线程池
        ：param max_num:线程池最大线程数量
        ：param max_task_num: 任务队列长度
        """
        # 设置队列 任务最大个数 默认无限长
        if max_task_num:
            self.q = queue.Queue(max_task_num)
        else:
            self.q = queue.Queue()
        # 最大线程数量
        self.max_num = max_num
        # 任务取消
        self.canncel = False
        # 任务关闭
        self.terminal = False
        # 已实例化的线程列表
        self.generate_list = []
        # 处于空闲状态的线程列表
        self.free_list = []

    def put(self, func, args, callback=None):
        """
        往任务队列里放入一个任务
        :param func: 任务函数
        :param args: 任务函数所需参数
        :param callback: 任务执行失败或成功后执行的回调函数，回调函数有两个参数
        1、任务函数执行状态；2、任务函数返回值（默认为None，即：不执行回调函数）
        :return: 如果线程池已经终止，则返回True否则None
        """
        # 任务是否已取消
        if self.canncel:
            return
        # 如果没有空闲线程，并且已创建的线程数量小于最大线程数量，创建新线程
        if len(self.free_list) == 0 and len(self.generate_list) < self.max_num:
            self.generate_thread()
        # 任务 函数，参数，回调函数
        task = (func, args, callback,)
        # 将任务放入队列
        self.q.put(task)

    def generate_thread(self):
        """
        创建新的线程
        """
        # 每个线程都执行call方法
        t = threading.Thread(target=self.call)
        t.start()

    def call(self):
        """
        循环去获取任务函数并执行任务函数。在正常情况下，
        每个线程都保存生存状态，直到获取线程终止的flag。
        """
        current_thread = threading.current_thread().name
        # 将当前线程添加到已实例化的线程列表中
        self.generate_list.append(current_thread)
        # 从任务队列里获取任务
        event = self.q.get()

        # 让获取的任务不是终止线程的标识对象时
        while event != StopEvent:
            # 获取任务中封装的三个参数
            func, arguments, callback = event
            
            # 抓取异常，防止线程因为异常退出
            try:
                result = func(current_thread, *arguments)
                success = True
            except Exception as e:
                result = None
                success = False
            
            # 如果有指定的回调函数
            if callback is not None:
                try:
                    callback(success, result)
                except Exception as e:
                    pass
            
            # 当某个线程正常执行完一个任务时，先执行worker_state方法
            with self.work_state(self.free_list, current_thread):
                # 如果强制关闭线程的flag开启，则传入一个StopEvent元素
                if self.terminal:
                    event = StopEvent
                # 否则获取一个正常的任务，重新开始循环
                else:
                    event = self.q.get()
            
        else:
            # 一旦发现任务是个终止线程的标识元素，将线程从已创建线程列表中删除
            self.generate_list.remove(current_thread)

    def close(self):
        """
        执行完所有的任务后，让所有线程都停止的方法
        """
        self.canncel = True

        full_size = len(self.generate_list)
        while full_size:
            self.q.put(StopEvent)
            full_size -= 1

    def terminate(self):
        """
        在任务执行过程中，终止线程，提前退出。
        """
        self.terminal = True
        while self.generate_list:
            self.q.put(StopEvent)

    @contextlib.contextmanager
    def work_state(self, state_list, work_thread):
        """
        用于记录空闲的线程，或从空闲列表中取出线程处理任务
        """
        state_list.append(work_thread)

        try:
            yield
        finally:
            state_list.remove(work_thread)


if __name__ == "__main__":
    pool = ThreadPool(5)

    for i in range(100):
        pool.put(lambda x: x**x, (i,))
