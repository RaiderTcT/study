#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Ulysses
@Date: 2019-10-29 09:22:46
@Description: 赋值, 拷贝
@LastEditTime: 2019-10-29 09:30:13
'''
import numpy as np


a = np.arange(9).reshape(3, 3)

# 都是浅拷贝, 引用
b = a
c = a
d = a

# 改变 a 的值 其他会改变
a[1,1] = 111
print(a)
"""
[[  0   1   2]
 [  3 111   5]
 [  6   7   8]]
"""
print(b[1, 1], c[1, 1])
# 111 111
print(d)
"""
[[  0   1   2]
 [  3 111   5]
 [  6   7   8]]
"""

# 改变d的值, 其他同样会变
d[-1, -1] = 0
print(d)
"""
[[  0   1   2]
 [  3 111   5]
 [  6   7   0]]
"""
print(c[-1, -1], b[-1, -1], a[-1, -1])
# 0  0  0

array = np.ones((2, 2))
# 使用copy函数
new_array = array.copy()
new_array[0, 0] = 111
print(array)
"""
[[1. 1.]
 [1. 1.]]
"""
