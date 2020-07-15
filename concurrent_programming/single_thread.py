import time



def worker(n):
    print(f"函数起始时间：{time.ctime()}")

    time.sleep(n)
    print(f"函数结束时间:{time.ctime()}")

def main():
    print(f"函数起始时间1：{time.ctime()}")
    worker(4)
    worker(2)
    print(f"函数结束时间1:{time.ctime()}")

if __name__ == "__main__":
    main()