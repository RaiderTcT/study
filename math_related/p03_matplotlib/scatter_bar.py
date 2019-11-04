#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Ulysses
@Date: 2019-11-04 15:38:46
@Description: 散点图, 柱状图
@LastEditTime: 2019-11-04 16:43:02
'''
import numpy as np
import matplotlib.pyplot as plt


def plot_scatter():
    n = 1024
    # 标注正态分布
    X = np.random.normal(0, 1, n)
    Y = np.random.normal(0, 1, n)

    T = np.arctan2(Y, X)  # 点的颜色
    print(T[500])
    plt.scatter(X, Y, s=50, c=T, alpha=0.7)
    plt.xlim((-3.5, 3.5))
    plt.xticks(())  # 隐藏xticks
    plt.ylim((-3.5, 3.5))
    plt.yticks(())  # 隐藏yticks

    plt.show()

def plot_bar():
    n = 12
    X = np.arange(n)
    uniform = np.random.uniform(0.5, 1.0, n)
    print(X, uniform)
    Y1 = (1-X/float(n)) * np.random.uniform(0.5, 1.0, n)  # 均匀分布
    Y2 = (1-X/float(n)) * np.random.uniform(0.5, 1.0, n)  # 均匀分布
    # 设置主题颜色和边框颜色
    plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
    plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

    plt.xlim(-2, n)
    plt.ylim(-1.25, 1.25)
    plt.xticks(())
    plt.yticks(())

    for x, y1 in zip(X, Y1):
        # ha: horizontal alignment
        # va: vertical alignment
        # 横向居中对齐，纵向底部（顶部）对齐
        plt.text(x+0.2, y1+0.05, f"{y1:.2}", ha='center', va='bottom')

    for x, y2 in zip(X, Y2):
        plt.text(x+0.2, -y2-0.05, f"{y2:.2}", ha='center', va='top')
    plt.show()


if __name__ == '__main__':
    # plt_scatter()
    plot_bar()
