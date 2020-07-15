import threading
import queue
import time


class MyThreadPool:
    """把线程类当做元素添加到队列内, 每个线程使用后就被抛弃"""
    def __init__(self, maxsize=5):
        self.maxsize = maxsize
        self._pool = queue.Queue(maxsize)  # 使用队列创建线程池
        for _ in range(maxsize):
            self._pool.put(threading.Thread)

    def get_thread(self):
        return self._pool.get(threading.Thread)

    def add_thread(self):
        self._pool.put(threading.Thread)


def run(i, pool):
    print("执行任务", i)
    time.sleep(1)
    pool.add_thread()


if __name__ == "__main__":
    pool = MyThreadPool(5)

    for i in range(20):
        t = pool.get_thread()
        obj = t(target=run, args=(i, pool))
        obj.start()

    print(f"活动的子线程数量：{threading.active_count() -1 }")
