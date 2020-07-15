#!/usr/bin/python3.6
from multiprocessing import Process, Queue, current_process, Pipe

def foo(q):
    q.put(f'{current_process().name}:hello')

def f(conn):
    conn.send(f"{current_process().name}: hello")
    conn.close()

if __name__ == '__main__':
    # q = Queue()
    # for i in range(3):
    #     p = Process(target=foo, args=(q,))
    #     p.start()
    #     p.join()
    # while not q.empty():
    #     print(q.get())
    parent_conn, child_conn = Pipe()
    for i in range(3):
        p = Process(target=f, args=(child_conn,))
        p.start()
        p.join()
    print(parent_conn.recv())
    print(parent_conn.recv())
    print(parent_conn.recv())