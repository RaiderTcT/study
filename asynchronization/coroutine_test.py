"""协程， 在一个线程内执行，在协程中控制共享资源不加锁，只需要判断状态
   子程序就是协程的一种特例
   Python对协程的支持是通过generator实现的
"""


def consumer():
    arg = 'Start...'
    while True:
        re = yield arg
        if not re:
            return
        print(f"[CONSUMER] Consuming {re}...")
        arg = '200 OK'


def produce(c):
    a = c.send(None)  # 预激活协程
    print(a)
    n = 0
    while n < 5:
        n = n + 1
        print(f'[PRODECER] Producing {n}...')
        # The send() method returns the next value yielded by the generator,
        # or raises StopIteration
        # if the generator exits without yielding another value
        # 返回arg， 将 yield arg 整体的值赋值为 n，运行arg= ‘200 ok’ ，yield 返回 arg
        r = c.send(n)
        print(f"[PRODECER] Consuming return {r}...")
    # consumer 没有正常的退出
    c.close()


if __name__ == "__main__":
    c = consumer()
    produce(c)
