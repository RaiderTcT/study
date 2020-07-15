from multiprocessing import Pool
import time
import os


def func(x):
    return x * x


if __name__ == '__main__':
    with Pool(processes=4) as pool:
        print(pool.map(func, range(10)))

        # print same numbers in arbitrary order
        for i in pool.imap_unordered(func, range(10)):
            print(i)

        # 异步执行func(20)
        res = pool.apply_async(func, (20, ))  # runs in *only* one process
        print(res.get(timeout=1))

        res = pool.apply_async(os.getpid, ())  # runs in *only* one process
        print("pid:", res.get(timeout=1))

        multi_res = [pool.apply_async(os.getpid, ()) for i in range(4)]
        print([res.get(timeout=1) for res in multi_res])

        # make a single worker sleep for 10 secs
        res = pool.apply_async(time.sleep, (2, ))
        try:
            print(res.get(timeout=3))
        except TimeoutError:
            print("We lacked patience and got a multiprocessing.TimeoutError")

        print("For the moment, the pool remains available for more work")

    print("pool被关闭")
