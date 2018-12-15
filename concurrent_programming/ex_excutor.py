"""
concurrent.future 应用

"""
import time

import concurrent.futures as cf

numbers = list(range(1, 11))


def cout(n):
    for i in range(int(1e7)):
        i += i
    return i * n


def worker(x):
    result = cout(x)
    print(f"数字：{x} 的结果 为 ：{result}")


# 顺序执行

def sequentital_execution():
    start_time = time.clock()

    for i in numbers:
        worker(i)
    print(f"顺序执行时间：{time.clock()-start_time}秒")


# 线程池执行

def threading_execution():
    start_time = time.clock()
    with cf.ThreadPoolExecutor(max_workers=5) as executor:
        for i in numbers:
            executor.submit(worker, i)
    print(f"线程池执行时间：{time.clock()-start_time}秒")


# 进程池执行

def process_execution():
    start_time = time.clock()
    with cf.ProcessPoolExecutor(max_workers=5) as executor:
        for i in numbers:
            executor.submit(worker, i)
    print(f"进程池执行时间：{time.clock()-start_time}秒")


if __name__ == '__main__':
    # sequentital_execution()
    # threading_execution()
    process_execution()
