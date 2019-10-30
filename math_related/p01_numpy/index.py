#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Ulysses
@Date: 2019-10-28 15:09:34
@Description: 索引
@LastEditTime: 2019-10-28 15:22:24
'''
import numpy as np


A = np.arange(1, 10)
print("一维索引", A[1], A[-1])
# 一维索引 2 9

A = np.arange(1, 10).reshape((3, 3))
print(A)
"""
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""

print(A[2])
# [7 8 9]

print("二维索引", A[1][1], A[2, 1])
# 二维索引 5 8

print("切片", A[1, 0:2])  # 行, 列
# 1行 0列和1列  [4 5]

# 迭代
for row in A:  # 按行
    print(row)
"""
[1 2 3]
[4 5 6]
[7 8 9]
"""

for column in A.T:  # 按列
    print(column)
"""
[1 4 7]
[2 5 8]
[3 6 9]
"""

print(A.flatten())  # 展开为一维
# [1 2 3 4 5 6 7 8 9]
for item in A.flat:  # 一个迭代器
    print(item, end=', ')
# 1, 2, 3, 4, 5, 6, 7, 8, 9,
