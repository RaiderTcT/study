#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 选择排序
@Date: 2019-09-09 21:02:46
@Author: Ulysses
@LastEditTime: 2019-09-09 21:11:11
'''


def select_sort(lst):
    """
    原地排序
    前段已排序 | 后段未排序
    """
    for i in range(len(lst) - 1):
        k = i
        for j in range(i, len(lst)):
            if lst[j].key < lst[k].key:  # k 为未排序部分的最小值的位置
                k = j
        if k != i:
            lst[k], lst[i] = lst[i], lst[k]


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

l = [r1, r2, r4, r3, r6, r5, r7]

select_sort(l)

for r in l:
    print(r)
