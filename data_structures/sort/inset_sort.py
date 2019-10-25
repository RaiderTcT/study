#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 插入排序
@Author: Ulysses
@Date: 2019-08-26 14:45:06
@LastEditTime: 2019-10-25 10:01:05
'''
"""
 不断地把一个个元素插入一个序列中
 已排序 i 未排序
"""
class Record:
    def __init__(self, t, s):
        self.key = t
        self.data = s
    def __str__(self):
        return f"{self.key}:{self.data}"

def insert_sort(lst):
    """简单查找插入"""
    for i in range(1, len(lst)):  # 只一个元素，认为已排序
        x = lst[i]
        j = i
        while j > 0 and lst[j-1].key > x.key:
            lst[j] = lst[j-1]  # 反向从与i最近的元素开始查找，确定插入的位置
            j -= 1
        lst[j] = x


def binary_search_index(l, i):
    low, high, mid = 0, i - 1, -1
    while low <= high:
        mid = (high + low) // 2
        if l[i].key >= l[mid].key:  # 相等时,新元素排在后面
            low = mid + 1
        else:
            high = mid -1
    return low


def binary_insert(l):
    """二分查找插入"""
    # 元素插入
    length = len(l)
    for i in range(1, length):  #从第2个元素开始，插入到前一部分元素中
        # 得到插入的位置
        # 0 -> i - 1 已排序
        # i ->   未排序
        index = binary_search_index(l, i)
        x = l[i]
        j = i - 1
        # index后的元素后移
        while j >= index:
            l[j+1] = l[j]  # 反向从与i最近的元素开始查找，确定插入的位置
            j -= 1
        l[index] = x

def shell_insert_sort(lst):
    """
    希尔排序属于插入类排序,是将整个有序序列分割成若干小的子序列分别进行插入排序。
    排序过程：先取一个正整数d1<n，把所有序号相隔d1的数组元素放一组，
    组内进行直接插入排序；然后取d2<d1，重复上述分组和排序操作；
    直至di=1，即所有记录放进一个组中排序为止。
    比较相隔较远距离（称为增量）的数，使得数移动时能跨过多个元素，
    则进行一次比较就可能消除多个元素交换
    时间复杂度: O(n^（1.3—2）)
    空间复杂度: O(1)
    稳定性:不稳定,是多次插入
    """
    n = len(lst)
    h = 1
    while h < n/3:
        h = 3 * h + 1
    while h >= 1:
        for i in range(h, n):
            j = i
            while j >= h and lst[j].key < lst[j-h].key:
                lst[j], lst[j-h] = lst[j-h], lst[j]
                j -= h
        h = h // 3
    # gap = n // 2
    # while gap >= 1:
    #     for i in range(gap, n):
    #         j = i
    #         while j - gap >= 0 and lst[j].key < lst[j-gap].key:
    #             lst[j], lst[j-gap] = lst[j-gap], lst[j]
    #             j -= gap
    #     gap //= 2


if __name__ == "__main__":
    r1 = Record(1, 'a')
    r2 = Record(3, 'b')
    r3 = Record(6, 'c')
    r4 = Record(4, 'e')
    r5 = Record(2, 'z')
    r6 = Record(3, 'f')

    l = [r1, r2, r3, r4, r5, r6]
    # binary_insert(l)
    shell_insert_sort(l)
    for r in l:
        print(r, end=', ')
