#!/usr/bin/python3.6
import multiprocessing as mp

def foo(q):
    q.put("hello")

if __name__ == '__main__':
    context = mp.get_context("fork")
    q = context.Queue()
    p = context.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()