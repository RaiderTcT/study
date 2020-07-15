"""
事件,这是线程之间通信的最简单机制之一：一个线程发出事件信号，其他线程等待它。
事件对象管理内部标志flag，可以使用set（）方法将其设置为true，并使用clear（）方法将其重置为false。
wait（）方法将阻塞，直到该标志为true。
"""
import threading
import time

event = threading.Event()


def lighter():
    green_time = 5  # 绿灯时间
    red_time = 5    # 红灯时间
    event.set()     # 设置标志为True
    while True:
        print("绿灯亮")
        time.sleep(green_time)
        event.clear()  # 清除标志 False
        print("红灯亮")
        time.sleep(red_time)
        event.set()


def run(name):
    while True:
        if event.is_set():  # 判断标志是否为True
            print(f"{name}通行")
            time.sleep(1)
        else:
            print(f'{name}遇到红灯，停')
            event.wait()  # 等待直到标志为True
            print(f"绿灯亮{name}，行驶")


if __name__ == "__main__":
    light = threading.Thread(target=lighter,)
    light.start()

    for name in ['奔驰', "宝马", "奥迪"]:
        car = threading.Thread(target=run, args=(name,))
        car.start()
