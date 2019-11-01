#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Ulysses
@Date: 2019-11-01 16:58:29
@Description: 坐标轴操作
@LastEditTime: 2019-11-01 17:30:33
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x**2

plt.figure()
plt.plot(x, y2)
plt.plot(x, y1, ':g')
plt.xlim((-1, 2))
plt.ylim((-2, 3))

# plt.show()
# 设定x, y轴 刻度
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
# 设置标签
plt.yticks([-2, 1.8, -1, 1.22, 3],
           ['$really\ bad$', '$bad$', '$normal$', '$good$', '$really\ good$'])

plt.show()
