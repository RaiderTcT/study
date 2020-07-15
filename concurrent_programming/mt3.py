import time
import threading
from MyThread import MyThread


def worker(n):
    # print(f"{threading.current_thread().name}:函数起始时间：{time.ctime()}")
    time.sleep(n)
    # print(f"{threading.current_thread().name}:函数结束时间:{time.ctime()}")


def main():
    print(f"函数起始时间1：{time.ctime()}")
    threads = []
    t1 = MyThread(worker, 'thread-1', (4,))
    threads.append(t1)

    t2 = MyThread(worker, 'thread-2', (2,))
    threads.append(t2)
    for t in threads:
        t.start()
    # for t in threads:
    #     t.join()
    # 等待结束
    # time.sleep(4)
    print(f"函数结束时间1:{time.ctime()}")


if __name__ == "__main__":
    main()
