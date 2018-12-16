"""
进程锁
"""
import multiprocessing as mp

def f(i, l):
    with l:
        print(f"hello world, {i}")


if __name__ == '__main__':
    lock = mp.Lock()

    for num in range(5):
        mp.Process(target=f, args=(num, lock)).start()

