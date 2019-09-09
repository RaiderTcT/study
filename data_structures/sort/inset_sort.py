#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 插入排序
@Date: 2019-09-09 20:40:53
@Author: Ulysses
@LastEditTime: 2019-09-09 21:02:30
'''
"""
不断地把一个个元素插入一个序列中
已排序 i 未排序
"""


def insert_sort(lst):
    for i in range(1, len(lst)):
        x = lst[i]
        j = i
        while j > 0 and lst[j-1].key > x.key:
            lst[j] = lst[j-1]  # 反向i->0, 查找合适的插入位置
            j -= 1
        lst[j] = x


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

insert_sort(l)

for r in l:
    print(r)
