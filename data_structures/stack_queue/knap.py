#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 简单递归问题
@Date: 2019-09-15 10:56:50
@Author: Ulysses
@LastEditTime: 2019-09-15 19:39:34
'''
"""
一个背包可放入重量未weight的物品, 现有n件物品的集合S, w0, w1, ... wn-1
选出若干件使其重量之和为weight
"""

# knap(weight, n) 代表问题的解, 考虑最后一件Wn-1是否选取
# 1. 最后一件不选, 那么knap(weight, n-1)的解就是knap(weight, n)的解
# 2. 不选, knap(weight-Wn-1, n-1)的解加上Wn-1 就是问题的解
# 按这样分析, 1: weight=0, 有解 2:weight<0,得不到解 3: weight > 0, 但没有物品了, 无解


def knap(weight, wlist, n):
    if weight == 0:
        return True
    if weight < 0 or (weight > 0 and n < 1):
        return False
    if knap(weight-wlist[n-1], wlist, n-1):
        print(f"Item{n}: {wlist[n-1]}")
        return True
    if knap(weight, wlist, n-1):
        return True
    else:
        return False


if __name__ == "__main__":
    tt_weight = 30
    weight_list = list(range(1, 10))
    ret = knap(tt_weight, weight_list, len(weight_list))
