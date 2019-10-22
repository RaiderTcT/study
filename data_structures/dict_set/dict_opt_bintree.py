#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Ulysses
@Date: 2019-10-21 11:34:55
@Description: 最佳二叉排序树,平均检索长度最小
@LastEditTime: 2019-10-22 10:13:25
'''
from data_structures.dict_set.dict_bintree import DictBinTree
from data_structures.tree.binary_tree import BinTreeNode
from data_structures.dict_set import Assoc
"""
二叉排序树->扩充二叉树->扩充二叉排序树的对称序列
(e0,v0,e1,v1, ..., en-1, vn-1, en)
pi: 内部节点频度
qi: 外部节点频度
"""


class DictOptBinTree(DictBinTree):
    """
    所有结点等概率分布
    平均检索长度E(n) = (IPL+EPL)/(2n+1)
        = (2*IPL+3n)/(2n+1)   IPL内部路径之和
    """
    def __init__(self, seq):
        super().__init__()
        data = sorted(seq)
        self._root = DictOptBinTree.buildOBT(data, 0, len(data)-1)

    @staticmethod
    def buildOBT(data, start, end):
        """
        构造最佳二叉排序树, 基本想法是左右子树的结点均匀分布,使用递归方式构造
        data表要是排序表
        """
        if start > end:
            # 空树
            return None
        mid = (start + end) // 2
        # 递归构造左右子树
        left = DictOptBinTree.buildOBT(data, start, mid-1)
        right = DictOptBinTree.buildOBT(data, mid+1, end)
        # 返回root结点(子树结点)
        return BinTreeNode(Assoc(*data[mid]), left, right)


# 不等概率, 计算带权路径长度,使用动态规划
def build_opt_btree(wp, wq):
    """
    最佳二叉排序树带权路径长度
    C(i, j) = W(i, j) + min{C(i, k) + C(k+1, j)|i<k<j-1}
    W(i, j) = qi + pi + qi+1 + ... + pj-1 + qj =
         pi + pi+1 + ... + pj-1 + qi + qi+1 + ... + qj-1 + qj
    1. 构造只包含一个内部节点的最佳树T(0, 1), T(1, 2) ... T(n-1, n)
    2. 基于1 构造包含2个内部节点的最佳树T(0, 2) ... T(n-2, n)
    ...
    n. 构造T(0, n)
    时间复杂度: O(n^3)
    空间: O(n^2)
    Args:
        wp (list[int]): n个内部结点的频度序列
        wq (list[int]): n+1个外部节点的频度
    Return:
        c 子树T(i, j)代价
        r 子树T(i, j)根节点下标
    """
    inf = float("inf")
    w = {}  # (i,j)内外交叉节点段权值之和
    r = {}  #  最佳子树T(i,j)的根节点p下标
    c = {}  # 子树T(i, j)代价
    num = len(wp) + 1
    for i in range(num):
        c[(i , i)] = 0
    if len(wq) != num:
        raise ValueError("参数错误")
    for i in range(num):  # 计算所有的w[(i,j)]
        w[(i, i)] = wq[i]  # 对角线qi元素
        for j in range(i+1, num):  # 只取上半部 j>i
            # w[i][j] = w[i][j-1]  pj-1 + qj
            w[(i, j)] = w[(i, j-1)] + wp[j-1] + wq[j]
    for i in range(0, num-1):  # 只有一个内部节点的最小树
        r[(i, i+1)] = i
        c[(i, i+1)] = w[(i, i+1)]  # qi + pi + qi+1

    for m in range(2, num):
        # 包含m个节点的最佳树(n-m+1)棵
        for i in range(0, num-m):
            k0, j = i, i+m
            wmin = inf  # 使得Ck(i,j)最小
            #  取 min{C(i, k) + C(k+1, j)|i<k<j-1
            for k in range(i, j):
                if c[(i, k)] + c[(k+1, j)] < wmin:
                    wmin = c[(i, k)] + c[(k+1, j)]
                    k0 = k
            # T(i, k) 和 T(k+1, j)这2棵子树构造的T(i,j)是最佳
            c[(i, j)] = w[(i, j)] + wmin
            r[(i, j)] = k0
    return c, r

if __name__ == '__main__':
    from random import randint
    l1 = [randint(1, 100) for _ in range(15)]
    l2 = [chr(ord('a') + i) for i in range(15)]
    d = list(zip(l1, l2))
    print(d)
    dict_opt = DictOptBinTree(d)
    dict_opt.print()
    print(dict_opt.serarch(11))

    wp = [2, 3, 4, 1, 5, 6]  # A-F频度 A<B<C...<F
    wq = [5, 1, 1, 4, 2, 6, 3]

    c, r = build_opt_btree(wp, wq)
    print("代价", c)
    print("根节点下标", r)
# 代价 {(0, 0): 0, (1, 1): 0, (2, 2): 0, (3, 3): 0, (4, 4): 0, (5, 5): 0, (6, 6): 0, (0, 1): 8, (1, 2): 5, (2, 3): 9, (3, 4): 7, (4, 5): 13, (5, 6): 15, (0, 2): 17, (1, 3): 18, (2, 4): 19, (3, 5): 25, (4, 6): 35, (0, 3): 37, (1, 4): 28, (2, 5): 42, (3, 6): 49, (0, 4): 47, (1, 5): 55, (2, 6): 66, (0, 5): 76, (1, 6): 79, (0, 6): 105}
# 根节点下标 {(0, 1): 0, (1, 2): 1, (2, 3): 2, (3, 4): 3, (4, 5): 4, (5, 6): 5, (0, 2): 0, (1, 3): 2, (2, 4): 2, (3, 5): 4, (4, 6): 5, (0, 3): 1, (1, 4): 2, (2, 5): 4, (3, 6): 4, (0, 4): 2, (1, 5): 4, (2, 6): 4, (0, 5): 2, (1, 6): 4, (0, 6): 4}

"""
                5(E4)
           /            \
        4(C2)           6(F5)
        /      \       /     \
     2(A0)     1(D3)  6(e5)  3(e6)
     /   \       /  \
  5(e0) 3(B1) 4(e3) 2(e4)
        /   \
      1(e1) 1(e2)
C(0, 6) = 105
"""
