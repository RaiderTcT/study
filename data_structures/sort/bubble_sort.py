#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 冒泡排序 交换排序
@Date: 2019-09-09 19:33:52
@Author: Ulysses
@LastEditTime: 2019-09-09 20:39:10
'''


def bubble_sort(lst):
    """比较相邻元素,发现元素逆序时就交换他们"""
    for i in range(len(lst)):
        found = False
        for j in range(1, len(lst) - i):
            if lst[j - 1].key > lst[j].key:
                lst[j-1], lst[j] = lst[j], lst[j-1]
                found = True
        if not found:
            break


class Record:
    def __init__(self, key, value):
        self.key = key
        self.num = value

    def __str__(self):
        return f"{self.key}:{self.num}"


r1 = Record(1, 'a')
r2 = Record(2, 'a')
r3 = Record(3, 'b')
r4 = Record(4, 'c')
r5 = Record(8, 'd')
r6 = Record(5, 'e')
r7 = Record(6, 'f')

l = [r1, r2, r3, r4, r5, r6, r7]

bubble_sort(l)

for r in l:
    print(r)
