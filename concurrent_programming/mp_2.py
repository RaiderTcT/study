#!/usr/bin/python3
import multiprocessing
import os

def foo():
    print(f"进程名字:{multiprocessing.current_process().name}")
    print(f"父进程：{os.getppid()}") # 父进程
    print(f"当前进程：{os.getpid()}")  # 子进程
    print("-"*10)

if __name__ == '__main__':
    print(f"当前进程id：{os.getpid()}")
    for i in range(5):
        p = multiprocessing.Process(target=foo)
        p.start()
