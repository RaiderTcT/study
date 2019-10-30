#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Ulysses
@Date: 2019-10-28 11:22:46
@Description: numpy 基础运算
@LastEditTime: 2019-10-30 23:15:32
'''
import numpy as np


a = np.array([10, 20, 30, 40])
b = np.arange(4)  # [0, 1, 2, 3]
c = np.arange(24).reshape((2, 3, 4))
print(a.shape)  # (4,)
print(c)
"""
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
"""
# 沿着指定轴(shape顺序)
print(np.amin(c, 1))  # 求一维数组对应的元素的最小值 shape是（2，4）
"""
[[ 0  1  2  3]
 [12 13 14 15]]
"""
print(c.min(0))  # 对2个二维数组求最小
"""
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
"""

# 40 [0 4 8]
# 一维矩阵
print("减", a - b)
# [10 19 28 37]

print("加", a + b)
# [10 21 32 43]

print("对应元素相乘", a * b)
# [  0  20  60 120]

print("每个元素的乘方", b ** 2)
# [0 1 4 9]

print("对每个元素求三角函数", np.sin(b))
#  [0.         0.84147098 0.90929743 0.14112001]

print("逻辑判断", b < 3)
# [ True  True  True False]

# 多维矩阵
a = np.arange(4).reshape((2, 2))  # [[0, 1], [2, 3]]
b = np.array([[1, 1], [0, 1]])

print("点乘 ab\n", np.dot(a, b))
"""
[[0 1]
 [2 5]]
"""

"""
矩阵乘法理解
矩阵A
a11 * x1 + a12 * x2 = y1
a21 * x1 + a22 * x2 = y2
 a11 a12    x1      y1
          *     =
 a21 a22    x2      y2
矩阵B
b11 * t1 + b12 * t2 = x1
b21 * t1 + b22 * t2 = x2
 b11 b12     t1     x1
          *      =
 b21 b22     t2     x2

将第二个带入第一个
(a11*b11 + a11*b12)*t1 + (a12*b11 + a12*b12)*t2 = y1
(a21*b21 + a21*b22)*t1 + (a22*b21 + a22*b22)*t2 = y1

a11 a12   b11 b12    a11*b11 + a11*b12  a12*b11 + a12*b12
        *          =
a21 a22   b21 b22    a21*b21 + a21*b22  a22*b21 + a22*b22
"""

print("点乘 b*a\n", b.dot(a))
"""
 [[2 4]
 [2 3]]
"""

rand_a = np.random.randint(1, 100, (2, 4))  # 随即生成2*4矩阵 范围1-100
print("rand_a", rand_a)
print(np.max(rand_a), np.min(rand_a), np.sum(rand_a), np.average(rand_a))
print("每一行最大", np.max(rand_a, axis=1))  # 1行为单元  0列为单元
print("每一列之和", np.sum(rand_a, axis=0))
a = np.arange(13, 1, -1).reshape((3, 4))
print("中值mean", np.mean(a), a.mean())
# 中值mean 7.5 7.5

print("从头累加尾", np.cumsum(a), a.cumsum())
# [13 25 36 46 55 63 70 76 81 85 88 90]
print("类差\n", np.diff(a))
"""
每一行中后一项与前一项之差
[[1 1 1]
 [1 1 1]
 [1 1 1]]
"""
print(np.nonzero(a))
# 将所有非零元素的行与列坐标分割开，重构成两个分别关于行和列的矩阵
# (array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2], dtype=int64),
#  array([0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3], dtype=int64))

# 排序 每一行或列
print("每一行排序\n", np.sort(a, axis=-1))
"""
[[10 11 12 13]
 [ 6  7  8  9]
 [ 2  3  4  5]]
"""
print("排序,展平", np.sort(a, axis=None))
# [ 2  3  4  5  6  7  8  9 10 11 12 13]

print("转置\n", a.T)  # np.transpose(A)
"""
[[13  9  5]
 [12  8  4]
 [11  7  3]
 [10  6  2]]
"""

print("clip\n", np.clip(a, 5, 9))  # 小于最小值或大于最大值的会被转为最大或最小值
"""
 [[9 9 9 9]
 [9 8 7 6]
 [5 5 5 5]]
"""
