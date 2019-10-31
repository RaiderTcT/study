#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Ulysses
@Date: 2019-10-31 17:04:36
@Description: matplotlib 的使用
@LastEditTime: 2019-10-31 17:32:13
'''
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-2 * np.pi, 2 * np.pi, 50)
y1 = x + 1
y2 = np.sin(x) + 1
plt.figure(num=3, figsize=(8, 5))  # 定义一个图像窗口

# 同一个坐标轴2个图像
plt.plot(x, y1)
plt.plot(x, y2, color='red', linestyle='--', linewidth=1.0)

# 设置坐标轴范围
plt.xlim((-np.pi, np.pi))
plt.ylim((-2.5, 4.5))

# 设置坐标轴名称
plt.xlabel('x')
plt.ylabel('y')

# 设置刻度
plt.xticks(np.linspace(-2.5, 4.5, 6))

plt.show()
