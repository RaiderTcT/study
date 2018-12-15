"""
类名：Condition
Condition称作条件锁，依然是通过acquire()/release()加锁解锁。
wait([timeout])方法将使线程进入Condition的等待池等待通知，并释放锁。
使用前线程必须已获得锁定，否则将抛出异常。
notify()方法将从等待池挑选一个线程并通知，收到通知的线程将自动调用acquire()尝试获得锁定（进入锁定池），
其他线程仍然在等待池中。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。
notifyAll()方法将通知等待池中所有的线程，这些线程都将进入锁定池尝试获得锁定。
调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。
"""
import threading
import time
num = 0
con = threading.Condition()


def switch():
    global num
    return True if num == 0 or num == 5 else False


class Foo(threading.Thread):

    def __init__(self, name, action):
        super().__init__()
        self.name = name
        self.action = action

    def run(self):
        global num
        with con:
            print(f"{self.name}开始执行")
            while True:
                if self.action == "add":
                    num += 1
                elif self.action == "reduce":
                    num -= 1
                else:
                    exit(1)  # 表示发生了错误
                print(f"num值为{num}")
                time.sleep(1)
                if num == 5 or num == 0:
                    print(f"{self.name}暂停执行！")
                    con.notify()  # 唤醒一个等待此条件的线程（如果有）
                    con.wait()  # 释放底层锁，然后阻塞，直到它被另一个线程中的相同条件变量的notify或notify_all唤醒
                    print(f"{self.name}开始执行")


if __name__ == "__main__":
    a = Foo("线程A", 'add')
    b = Foo("线程B", 'reduce')
    a.start()
    b.start()
