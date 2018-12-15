"""
后进先出队列
"""
import random
import time
import queue
import threading

q = queue.LifoQueue()
for i in range(5):
    if not q.full():
        q.put(i)
        print(f"放入元素{i}")
while not q.empty():
    print(f"取出元素{q.get()}")