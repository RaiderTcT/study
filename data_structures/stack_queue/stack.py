#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 栈的实现, FILO, 在一端插入和删除
@Date: 2019-09-11 20:06:10
@Author: Ulysses
@LastEditTime: 2019-09-11 20:38:46
'''
from data_structures.linklist.linkedlist import LNode


class StackUnderflow(ValueError):
    pass


class SStack:  # 委托, 基于顺序表实现
    def __init__(self):
        self._stack = []

    def is_empty(self):
        return self._stack == []

    def top(self):
        if self._stack == []:
            raise StackUnderflow
        return self._stack[-1]

    def pop(self):
        if self._stack == []:
            raise StackUnderflow
        return self._stack.pop()

    def push(self, x):
        self._stack.append(x)


class LStack:
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise StackUnderflow
        return self._top.elem

    def pop(self):
        if self._top is None:
            raise StackUnderflow
        p = self._top
        self._top = p.next
        return p.elem

    def push(self, x):
        self._top = LNode(x, self._top)


if __name__ == "__main__":
    st1 = SStack()
    st1.push(1)
    st1.push(2)
    while not st1.is_empty():
        print(st1.pop())

    st1 = LStack()
    st1.push(1)
    st1.push(2)
    while not st1.is_empty():
        print(st1.pop())
