#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 归并排序
@Date: 2019-09-10 19:41:57
@Author: Ulysses
@LastEditTime: 2019-09-10 20:55:38
'''
"""
二路归并
1. 把排序的序列中的n个记录看成n个有序子序列,长度各为1
2. 把当时序列组里的有序子序列两两归并, 完成一次后序列里的排序序列个数减少到一半
每个子序列长度加倍
3. 对加长的子序列重复进行上面操作

三层处理
1. 最下层: 实现表中相邻一对有序序列的归并,并将归并结果存入另一个顺序表的相同位置
2. 中间层: 对表中各有序序列的归并, 完成一遍后存入另一个顺序表的相同位置分段
3. 最上层: 在2个顺序表之间往复执行2,一遍后交换2个表的地位,重复2,直到整个表里只有一个有序序列
O(nlogn)
"""


def merge(lfrom, lto, low, mid, high):
    """
    最下一层
    连续排放的2分有序序列的归并
    lfrom[low:mmid] lfrom[mid:high]
    """
    i, j, k = low, mid, low
    while i < mid and j < high:
        if lfrom[i] <= lfrom[j]:  # 选取2段中较小的值到新表
            lto[k] = lfrom[i]
            i += 1
        else:
            lto[k] = lfrom[j]
            j += 1
        k += 1
    # 处理 剩余的元素（保留下的是最大的几个值）

    # 第一段剩余，复制
    # while i < mid:
    #     lto[k] = lfrom[i]
    #     i += 1
    #     k += 1
    # while j < high:
    #     lto[k] = lfrom[j]
    #     j += 1
    #     k += 1

    if i < mid:
        lto[k:high] = lfrom[i:mid]
    if j < high:
        lto[k:high] = lfrom[j:high]


def merge_pass(lfrom, lto, llen, slen):
    """
    一对对分段的归并
    Args:
        lfrom ([type]): 被归并的有序段
        lto ([type]): 归并结果保存的位置
        llen ([type]): 表长度
        slen ([type]): 分段的长度
    """
    i = 0
    while i + 2 * slen < llen:
        merge(lfrom, lto, i, i+slen, i + 2*slen)
        i += 2 * slen
    if i + slen < llen:  # 剩余部分超过分段长度
        merge(lfrom, lto, i, i+slen, llen)
    else:
        for j in range(i, llen):  # 复制最后一小段
            lto[j] = lfrom[j]


def merge_sort(lst):
    slen, llen = 1, len(lst)
    temp_list = [None] * llen
    while slen < llen:
        merge_pass(lst, temp_list, llen, slen)
        slen *= 2
        merge_pass(temp_list, lst, llen, slen)
        slen *= 2


if __name__ == "__main__":
    import random
    l = []
    for i in range(10):
        l.append(random.randint(0, 100))
    print(l)
    merge_sort(l)
    print(l)


