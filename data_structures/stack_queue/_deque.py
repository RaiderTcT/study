#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 自定义的双端队列, double end queue
@Date: 2019-09-15 19:40:56
@Author: Ulysses
@LastEditTime: 2019-09-15 20:02:10
'''
from data_structures.linklist.dllist import DLList


class DequeUnderflower(ValueError):
    pass


class Deuqe_dl:  # 基于双端链表
    def __init__(self):
        self._deque = DLList()

    def pop(self):
        if not self._deque.is_empty():
            return self._deque.pop_last()

    def is_empty(self):
        return self._deque.is_empty()

    def pop_left(self):
        if not self._deque.is_empty():
            return self._deque.pop_first()

    def append(self, x):
        self._deque.append(x)

    def append_left(self, x):
        self._deque.prepend(x)


class Deque_cl:  # 基于循环列表
    def __init__(self, init_len=8):
        self._len = init_len
        self._elems = [None] * init_len
        self._head = 0
        self._num = 0

    def is_empty(self):
        return self._num == 0

    def qsize(self):
        return self._num

    def pop(self):
        if self._num == 0:
            raise DequeUnderflower
        e = self._elems[(self._head + self._num - 1) % self._len]
        self._num -= 1
        return e

    def pop_left(self):
        if self._num == 0:
            raise DequeUnderflower
        e = self._elems[self._head]
        self._head = (self._head + 1) % self._len
        self._num -= 1
        return e

    def __extend(self):
        old_len = self._len
        self._len = old_len * 2
        new_elems = [None] * self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head + i) % old_len]
        self._elems, self._head = new_elems, 0

    def append(self, x):
        if self._num == self._len:
            self.__extend()
        self._elems[(self._head + self._num) % self._len] = x
        self._num += 1

    def append_left(self, x):
        if self._num == self._len:
            self.__extend()
        self._head = (self._head - 1 + self._len) % self._len
        self._elems[self._head] = x
        self._num += 1


if __name__ == "__main__":
    dq = Deque_cl()
    for i in range(10):
        dq.append(i)
    dq.append_left('x')
    print(dq.pop())
    print(dq.pop_left())
