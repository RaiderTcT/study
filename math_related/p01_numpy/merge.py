#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Ulysses
@Date: 2019-10-28 15:44:49
@Description: 矩阵合并操作
@LastEditTime: 2019-10-28 16:37:07
'''
import numpy as np


"""
1. concatenate 沿着现存的轴连接数据序列
2. stack 沿着新轴连接数组序列
3. hstack 水平堆叠序列中的数组（列方向）
4. vstack 竖直堆叠序列中的数组（行方向）
"""

A = np.array([1, 2, 3 ,4])
B = np.array([2, 4, 6, 8])

print("沿新轴0堆叠两个数组\n", np.stack((A, B), axis=0))
"""
 [[1 2]
 [2 4]
 [3 6]
 [4 8]]
"""

print("沿新轴1堆叠两个数组\n", np.stack((A, B), axis=1))
"""
[[1 2 3 4]
 [2 4 6 8]]
"""

print(np.vstack((A, B)))  # 垂直（行）按顺序堆叠数组。
"""
[[1 2 3 4]
 [2 4 6 8]]
"""

C = np.hstack((A, B))  # 水平（按列）顺序堆叠数组。
print(C)  # [1 2 3 4 2 4 6 8]

print(A)
# [1 2 3 4]

print(A[np.newaxis, :])  # 将 A 转为1行 4列
# [[1 2 3 4]]

new_array = A[:, np.newaxis]  # 4行 1列
print(new_array, new_array.shape)
"""
[[1]
 [2]
 [3]
 [4]]
"""

A = np.array([1, 1, 1])[:, np.newaxis]
B = np.array([2, 2, 2])[:, np.newaxis]

C = np.vstack((A, B))  # vertical stack  垂直
D = np.hstack((A, B))  # horizontal stack  水平堆叠
print(C.shape, C)
"""
(6, 1)
[[1]
 [1]
 [1]
 [2]
 [2]
 [2]]
"""
print(D.shape, D)
"""
(3, 2)
[[1 2]
 [1 2]
 [1 2]]

"""

# 合并多个矩阵

print(np.concatenate((A, B, B, A), axis=0))  # 0 在垂直方向上堆叠 按行
"""
[[1]
 [1]
 [1]
 [2]
 [2]
 [2]
 [2]
 [2]
 [2]
 [1]
 [1]
 [1]]
"""

print(np.concatenate((A, B, B, A), axis=1))  # 1 水平方向堆叠 按列
"""
[[1 2 2 1]
 [1 2 2 1]
 [1 2 2 1]]
"""
