import time
import threading

def worker(n):
    print(f"{threading.current_thread().name}函数起始时间：{time.ctime()}")

    time.sleep(n)
    print(f"{threading.current_thread().name}函数结束时间:{time.ctime()}")

def main():
    print(f"函数起始时间1：{time.ctime()}")
    threads = []
    t1 = threading.Thread(target=worker, name='thread_mt_1', args=(4,))
    # t1.daemon = True
    threads.append(t1)
    t2 = threading.Thread(target=worker, name='thread_mt_2', args=(2,))
    # t2.daemon = True
    threads.append(t2)
    for t in threads:
        t.start()
    # 主线程等待子线程
    # t1.join(timeout=3)
    t1.join()
    t2.join()
    print(f"函数结束时间1:{time.ctime()}")

if __name__ == "__main__":
    main()
