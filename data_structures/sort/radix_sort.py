#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 分配排序
@Date: 2019-09-10 20:56:23
@Author: Ulysses
@LastEditTime: 2019-09-11 20:02:24
'''
"""
基于固定位置的分配和收集,如果关键码只有很少几个不同的值,
1. 为每个关键码值设定一个 桶(能容纳任意多个记录的容器)
2. 排序时简单地根据关键码将记录放入相应桶中
3. 存入所有桶后,顺序收集各个桶里的记录,就得到排序的序列
O(n)
多轮分配排序-基数排序:以元组未关键码,通过多轮分配和收集
"""


class Record:
    def __init__(self, key, value):
        self.key = key
        self.num = value

    def __str__(self):
        return f"{self.key}:{self.num}"


def radix_sort(lst, d):
    rlist = [[] for i in range(10)]
    llen = len(lst)
    # 从关键码的最低位(x.key[-1])开始工作,逐位向上,直至排序完成
    # 按后一位排序收集完后的序列,再按前一位key排序后,相同key(前一位)的子序列能保持后一位有序
    for m in range(-1, -d-1, -1):
        for j in range(llen):
            # 把一记录分配到桶中
            rlist[lst[j].key[m]].append(lst[j])
        j = 0
        for i in range(10):
            temp = rlist[i]
            for k in range(len(temp)):
                lst[j] = temp[k]
                j += 1
            rlist[i].clear()

if __name__ == "__main__":
    r1 = Record((0, 1, 2), 'a')
    r2 = Record((0, 1, 3), 'a')
    r3 = Record((1, 1, 3), 'b')
    r4 = Record((0, 2, 4), 'c')
    r5 = Record((0, 2, 3), 'd')
    r6 = Record((1, 1, 6), 'e')
    r7 = Record((1, 1, 5), 'f')

    l = [r1, r2, r4, r3, r6, r5, r7]
    radix_sort(l, 3)
    for r in l:
        print(r)
