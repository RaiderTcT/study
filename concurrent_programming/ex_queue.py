"""
    FIFO队列
"""
import threading
import queue
import time
import random
from dataclasses import dataclass, field


def producer(data_queue):
    for i in range(5):
        time.sleep(0.5)
        item = random.randint(1, 100)
        data_queue.put(item)
        print(f'{threading.current_thread().name} 在队列放入{item}')


def consumer(data_queue):
    while True:
        try:
            item = data_queue.get(timeout=3)
            print(f"{threading.current_thread().name}移除出队列{item}")
        except queue.Empty:
            break
        else:
            data_queue.task_done()


def main():
    q = queue.Queue()

    threads = []

    p = threading.Thread(target=producer, args=(q,))
    p.start()

    for i in range(2):
        c = threading.Thread(target=consumer, args=(q,))
        threads.append(c)

    for t in threads:
        t.start()

    q.join()  # Blocks until all items in the queue have been gotten and processed.


if __name__ == "__main__":
    main()
