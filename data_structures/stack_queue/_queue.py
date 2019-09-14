#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 队列的实现  FIFO
@Date: 2019-09-14 15:36:07
@Author: Ulysses
@LastEditTime: 2019-09-14 16:02:21
'''
from data_structures.linklist.linkedlist_1 import LList1


class QueueUnderflow(ValueError):
    pass


class LQueue:
    """基于带尾指针的链表"""
    def __init__(self):
        self._llist = LList1()

    def is_empty(self):
        return self._llist.is_empty()

    def peek(self):
        if self.is_empty():
            raise QueueUnderflow
        return self._llist._head.elem

    def get(self):
        if not self.is_empty():
            return self._llist.pop_first()

    def put(self, x):
        self._llist.append(x)

    def qsize(self):
        return self._llist.count


# 基于循环列表实现, O(n)首端插入, O(1)尾端获取
class SQueue:
    def __init__(self, init_len=8):
        self._len = init_len
        self._elems = [0] * init_len
        self._head = 0
        self._num = 0

    def is_empty(self):
        return self._num == 0

    def qsize(self):
        return self._num

    def peek(self):
        if self._num == 0:
            raise QueueUnderflow
        return self._elems[self._head]

    def get(self):
        if self._num == 0:
            raise QueueUnderflow
        e = self._elems[self._head]
        self._head = (self._head + 1) % self._len
        self._num -= 1
        return e

    def __extend(self):
        old_len = self._len
        self._len = old_len * 2
        new_elems = [0] * self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head + i) % old_len]
        self._elems, self._head = new_elems, 0

    def put(self, x):
        if self._num == self._len:
            self.__extend()
        self._elems[(self._head + self._num) % self._len] = x
        self._num += 1


if __name__ == "__main__":
    q1 = SQueue()
    for i in range(10):
        q1.put(i)
    print(q1.qsize())
    print(q1.peek())
    print(q1.get())
