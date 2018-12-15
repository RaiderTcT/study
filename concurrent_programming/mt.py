import time
import _thread


def worker(n):
    print(f"函数起始时间：{time.ctime()}")

    time.sleep(n)
    print(f"函数结束时间:{time.ctime()}")

def main():
    print(f"函数起始时间1：{time.ctime()}")
    _thread.start_new_thread(worker, (4,))
    _thread.start_new_thread(worker, (2,))
    time.sleep(4)
    print(f"函数结束时间1:{time.ctime()}")

if __name__ == "__main__":
    main()