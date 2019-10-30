#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Ulysses
@Date: 2019-10-29 08:43:12
@Description: 矩阵的分割
@LastEditTime: 2019-10-29 09:21:11
'''
import numpy as np


array = np.arange(12).reshape(3, 4)
print(array)

"""
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
"""

print("纵向分割\n", np.split(array, 2, axis=1))  # 1沿着纵轴分割 分成2部分
"""
 [array([[0, 1],
       [4, 5],
       [8, 9]]), array([[ 2,  3],
       [ 6,  7],
       [10, 11]])]
"""

print("横向分割\n", np.split(array, 3, axis=0))  # 0按横轴分割 分成3部分
#  [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]

array1 = np.arange(20).reshape(5, 4)
print("界定分割后范围\n", np.split(array1, [2, 3], axis=0))
# 三部分  [:2]  [2:3]  [3:]
"""
 [array([[0, 1, 2, 3],
       [4, 5, 6, 7]]), array([[ 8,  9, 10, 11]]), array([[12, 13, 14, 15],
       [16, 17, 18, 19]])]
"""

print("不等量分割\n", np.array_split(array1, 3, axis=1))

"""
 [array([[ 0,  1],
       [ 4,  5],
       [ 8,  9],
       [12, 13],
       [16, 17]]), array([[ 2],
       [ 6],
       [10],
       [14],
       [18]]), array([[ 3],
       [ 7],
       [11],
       [15],
       [19]])]
"""

print("vsplit, 垂直方向上分割\n", np.vsplit(array1, 5))
# np.split(array1, 2, axis=0)  vertically (row-wise)
#  [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]]), array([[12, 13, 14, 15]]), array([[16, 17, 18, 19]])]
print("hsplit, 水平方向上分割\n", np.hsplit(array1, np.array([1, 2])))
"""
 [array([[ 0],
       [ 4],
       [ 8],
       [12],
       [16]]), array([[ 1],
       [ 5],
       [ 9],
       [13],
       [17]]), array([[ 2,  3],
       [ 6,  7],
       [10, 11],
       [14, 15],
       [18, 19]])]
"""
