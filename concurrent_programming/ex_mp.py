"""
多进程
"""
import time
import multiprocessing
import os 

def func(n):
    print(f"{multiprocessing.current_process().name} :{os.getpid()} 开始{time.ctime()}")
    time.sleep(n)
    print(f"{multiprocessing.current_process().name} :{os.getpid()} 结束{time.ctime()}")


def main():
    print(f"主函数起始：{time.ctime()}")

    process = []

    p1 = multiprocessing.Process(target=func, args=(4,))

    process.append(p1)

    p2 = multiprocessing.Process(target=func, args=(2,))

    process.append(p2)

    for p in process:
        p.start()

    for p in process:
        p.join()

    # 8个逻辑处理器，其中一个进程会等待完成后进行
    p = multiprocessing.Pool(8)
    for i in range(9):
        p.apply_async(func, args=(i+1,))
    p.close()
    p.join()
    print(f"主函数结束：{time.ctime()}")

if __name__ == '__main__':
    main()
