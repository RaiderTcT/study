#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Ulysses
@Date: 2019-10-22 10:22:54
@Description: 平衡二叉树AVL树
@LastEditTime: 2019-10-23 17:07:50
'''
from data_structures.dict_set import Assoc
from data_structures.tree.binary_tree import BinTreeNode
from data_structures.dict_set.dict_bintree import DictBinTree
# 有保证的O(logn)检索效率->二叉树高度始终维持logn->基本考虑:
# 每个结点左右子树高度差不多


class AVLNode(BinTreeNode):
    # 添加一个bf 平衡因子
    def __init__(self, data):
        super().__init__(data)
        self.bf = 0


class DictAVL(DictBinTree):

    @staticmethod
    def LL(a, b):
        """
        恢复操作 失衡和调整
        左子树较高,新节点插在a节点左子树b的左子树,再把b提升为根节点
        Args:
            a ([type]): 最小非平衡子树根节点 bf=1
            b ([type]): a的左子树(新节点要插入b的左子树) bf=0
        Returns:
            [type]: 调整后的子树根节点b
        """
        a.left = b.right
        b.right = a
        a.bf = b.bf = 0
        return b

    @staticmethod
    def RR(a, b):
        # 与 LL 相对应
        a.right = b.left
        b.left = a
        a.bf = b.bf = 0
        return b

    @staticmethod
    def LR(a, b):
        """
        a左子树较高, 插入节点在a的左子树b的右子树c下
        把c升为根节点, c的左右子树移到a和b下
        Args:
            a ([type]): [description]
            b ([type]): [description]

        Returns:
            [type]: 新的子树根节点
        """
        c = b.right
        a.left, b.rigth = c.right, c.left
        c.left, c.right = b, a
        if c.bf == 0:  #  c 本身就是插入节点
            a.bf = b.bf = 0
        elif c.bf == 1:  # 新节点在c左子树
            a.bf = -1
            b.bf = 0
        else:
            a.bf = 0
            b.bf = 1
        c.bf = 0
        return c

    @staticmethod
    def RL(a, b):
        # 与LR对应
        c = b.left
        a.right, b.left = c.left, c.right
        c.left, c.right = a, b
        if c.bf == 0:
            a.bf = 0
            b.bf = 0
        elif c.bf == -1:  # 新节点在c的右子树C
            a.bf = 1
            b.bf = 0
        else:   # 新节点在c的左子树B
            a.bf = 0
            b.bf = -1
        c.bf = 0
        return c

    def insert(self, key, value):
        """
        插入节点:
        1. 找到插入位置并实际插入新节点
        2. 修改一些节点的平衡因子
        3. 失衡时做局部调整
        a 距离插入位置最近的bf非0的节点, pa记录a的父节点
        p 扫描变量  q为p的父节点
        时间复杂度: O(logn) 不超过树的深度
        Args:
            key ([type]): [description]
            value ([type]): [description]
        """
        a = p = self._root
        node = AVLNode(Assoc(key, value))  # 要插入的节点
        if a is None:  # 原先为空树
            self._root = node
            return
        pa = q = None
        # 寻找插入的位置及最小非平衡子树
        while p is not None:
            if key == p.data.key:
                p.data.value = value  # 已存在的key,更新value
                return
            if p.bf != 0:
                pa, a = q, p  # 找到最小非平衡子树位置
            q = p
            if key < p.data.key:
                p = p.left
            else:
                p = p.right
        # q 插入点的父节点(叶节点) pa,a 记录最小非平衡子树
        if key < q.data.key:  # 作为左子树或右子树插入
            q.left = node
        else:
            q.right = node
        # 新节点插入后, a是最小不平衡子树
        if key < a.data.key:
            p = b = a.left  # 新节点在a的左子树
            d = 1
        else:
            p = b = a.right  # 新节点在a的右子树
            d = -1  # d 记录 新节点在a的那颗子树上
        # 沿着b(a子树) -> 新插入节点node 修改BF值
        while p != node:
            if key < p.data.key:  # 插入位置在p左子树,
                p.bf = 1
                p = p.left
            else:
                p.bf = -1
                p = p.right
        if a.bf == 0:  # bf原先为0, 插入一个节点后1 或 -1 不会失衡
            a.bf = d
            return
        if a.bf == -d:  # 新节点插入在较低的子树, 也不需要调整
            a.bf = 0
            return
        # 新节点插入在较高的子树下, 调整
        if d == 1:   # 新节点在a的左子树
            if b.bf == 1:  # 左子树较高
                b = DictAVL.LL(a, b)
            else:
                b = DictAVL.LR(a, b)
        else:  # 插到右子树
            if b.bf == -1:  # 右子树较高
                b = DictAVL.RR(a, b)
            else:
                b = DictAVL.RL(a, b)
        # 调整后的b是这部分子树的根, 再作为到pa的子树
        if pa is None:  # 原先的a就是根节点, 要修改_root
            self._root = b
        else:
            if pa.left == a:
                pa.left = b
            else:
                pa.right = b

    def delete(self, key):
        pass

    def depth(self):
        """
        调用递归函数计算深度
        """
        def depth0(t):
            if t is None:
                return 0
            return max(depth0(t.left), depth0(t.right)) + 1
        return depth0(self._root)

if __name__ == "__main__":
    from random import randint
    l1 = list(range(100))
    l2 = [str(i) for i in l1]
    d = list(zip(l1, l2))
    dict_avl = DictAVL()
    for key, value in d:
        dict_avl.insert(key, value)
    # dict_avl.print()
    print(dict_avl.serarch(l1[0]))
    print(dict_avl.depth())  # 高度 7
