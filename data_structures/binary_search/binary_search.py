#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 二分查找法
@Date: 2019-09-09 18:13:50
@Author: Ulysses
@LastEditTime: 2019-09-09 19:28:25
'''

# 适用有序的序列
def binary_search(l, item):
    """返回查找的值的下标"""
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = int((low + high) / 2)
        guess = l[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


def binary_rec(l, start, end, item):
    if start > end:
        return None
    else:
        mid = int((start + end) / 2)

        guess = l[mid]
        if guess == item:
            return mid
        elif guess > item:
            binary_rec(l, start, mid - 1, item)
        else:
            binary_rec(l, mid + 1, end, item)


def binary_search_1(l, item):
    return binary_rec(l, 0, len(l) - 1, item)


l = [1, 2, 3, 4, 5, 6, 7, 8]
print(binary_search_1(l, 4))
