#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 分配排序
@Date: 2019-09-10 20:56:23
@Author: Ulysses
@LastEditTime: 2019-09-10 20:57:58
'''


class Record:
    def __init__(self, key, value):
        self.key = key
        self.num = value

    def __str__(self):
        return f"{self.key}:{self.num}"

if __name__ == "__main__":
    r1 = Record(1, 'a')
    r2 = Record(2, 'a')
    r3 = Record(3, 'b')
    r4 = Record(4, 'c')
    r5 = Record(8, 'd')
    r6 = Record(5, 'e')
    r7 = Record(6, 'f')

    l = [r1, r2, r4, r3, r6, r5, r7]
