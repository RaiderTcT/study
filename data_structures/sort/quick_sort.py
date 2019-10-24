#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 快速排序
@Date: 2019-09-10 19:10:07
@Author: Ulysses
@LastEditTime: 2019-09-10 19:40:32
'''
"""
1. 选取基准值
2. 将数组分为两个子组:小于基准值的  大于基准值的
3. 对这两个子数组进行排序
"""


def quick_sort(array):
    """
    平均 O(nlogn), 最慢O(n*n)
    """
    if len(array) == 0:
        return   # 空return 结束生成器
    elif len(array) == 1:
        yield array[0]
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]
        yield from quick_sort(less)
        yield pivot
        yield from quick_sort(greater)


def quick_rec(lst, left, right):
    """递归版本"""
    if left >= right:
        return
    i = left
    j = right
    pivot = lst[i]  # 最初始空位置
    while i < j:
        while i < j and lst[j] >= pivot:  # 从最右向左找比基准值小的值
            j -= 1
        if i < j:
            lst[i] = lst[j]  # 移动到最左边, j位置空了
            i += 1
        while i < j and lst[i] <= pivot:   # 从最左向右找比基准值大的值
            i += 1
        if i < j:
            lst[j] = lst[i]  # 移动到ｊ位置
    lst[i] = pivot  # while循环后 i指向空位置
    quick_rec(lst, left, i - 1)
    quick_rec(lst, i + 1, right)

def quick_sort_2(lst):
    """
    R |<=R | >=R |????
           i     j
    """
    def qsort(lst, begin, end):
        if begin >= end:
            return
        pivot = lst[begin]
        i = begin
        for j in range(begin + 1, end + 1):
            if lst[j] < pivot:  # 把比pivot小的移动到前面,后面的都是大于pivot的
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        # begin位置是基准值, i位置是最后一个比基准值小的下标
        lst[begin], lst[i] = lst[i], lst[begin]
        qsort(lst, begin, i - 1)
        qsort(lst, i + 1, end)

    qsort(lst, 0, len(lst) - 1)    


if __name__ == "__main__":
    g = quick_sort([1, 7, 2, 5, 4, 3, 0, 8])
    for i in g:
        print(i, end=', ')
    print('')
    l = [1, 7, 2, 5, 4, 3, 0, 8]
    quick_rec(l, 0, len(l)-1)
    print(l)
