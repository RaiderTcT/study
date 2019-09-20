#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 二叉树
@Date: 2019-09-18 20:55:09
@Author: Ulysses
@LastEditTime: 2019-09-19 20:47:34
'''
from data_structures.stack_queue._queue import SQueue
from data_structures.stack_queue.stack import SStack
"""
树形结构tree由结点（结构中的逻辑单元，可用于保存数据）和结点之间的
连接关系（一种后继关系）构成， 特征：
1. 不为空则有唯一起始结点，称为树根root
2. 除root外，其余结点都只有一个前驱，有0个或多个后继，
一定有些结点并不连接其他结点
3. 从root结点出发经过若干次后继关系可以到达任意一个结点
4. 结点之间的联系不会形成循环关系
5. 从这种结构里的任意两个不同结点出发，通过后继关系可达的两个结点集合，或者
互不不相交，或者一个集合是另一个集合的子集

二叉树：结点关联的结点数可以为0，1或2，后继结点：左关联结点、右关联结点
空树：不包含任何结点
单点树：只包含一个根结点
树叶结点：两棵子树都为空，其余结点为 分支结点
度数：子节点个数，二叉树度数0、1或2
路径：从祖先结点到其任何子孙结点都存在一系列边，这种首尾相连的边称为树中一条路径，
路径中边的长度称为该路径的长度，从二叉树的根结点出发到树中任一结点都有路径，而且唯一。
层：二叉树是一种层次结构，根节点的层数为0，其子节点为下一层元素
高度（深度）：树中节点的最大层数-最长路径的长度

性质
非空二叉树，第i层 最多有2^i个结点
高度为h的二叉树，至多有2^(h+1) - 1个结点

非空二叉树中：叶结点个数为n0, 度数为2的结点个数为n2,有n0=n2+1
满二叉树：二叉树中所有分支结点的度数都是2，满二叉树里叶节点比分支结点多1个

扩充二叉树：对二叉树T，加入足够多的新叶结点，使T的原有结点都变成度数为2的
分支结点，得到的二叉树称为T的扩充二叉树
扩充二叉树的外部路径E（root到各外部结点的路径长度和），内部路径长度l，如果有
n个内部结点 -> E=l+2*n

完全二叉树：高度为h，从第0层到第h-1层的结点都满，如果最下一层不满，所有结点在最
左边连续排列，空位都在右边

n个结点的完全二叉树高度h = [log2n]，即不大于log2n的最大整数
"""

class BinaryTree:  # 使用python的list或tuple实现
    def __init__(self, data, left=None, right=None):
        self.tree = [data, left, right]

    def is_empty(self):
        return self.tree[0] is None

    def left_child(self):
        if not self.is_empty():
            return self.tree[1]

    def right_child(self):
        if not self.is_empty():
            return self.tree[2]

    def traversal(self):
        for data in self.tree:
            if not isinstance(data, type(self)):
                print(data)
            else:
                data.traversal()


class BinTreeNodeError(ValueError):
    pass


class BinTNode:  # 使用链接方法实现
    def __init__(self, dat, left=None, right=None):
        self.data = dat
        self.left = left
        self.right = right


def count_BinTNodes(t):
    if t is None:
        return 0
    else:
        return 1 + count_BinTNodes(t.left) + count_BinTNodes(t.right)


def sum_BinTNodes(t):
    if t is None:
        return 0
    else:
        return t.dat + sum_BinTNodes(t.left) + sum_BinTNodes(t.right)


def preorder(t, proc):
    """遍历 递归的方式 先根DLR"""
    if t is None:
        return
    assert(isinstance(t, BinTNode))
    proc(t.data)
    preorder(t.left, proc)
    preorder(t.right, proc)


def inorder(t, proc):
    """遍历 递归的方式 中根LDR"""
    if t is None:
        return
    inorder(t.left, proc)
    proc(t.data)
    inorder(t.right, proc)


def postorder(t, proc):
    """遍历 递归的方式 后根LDR"""
    if t is None:
        return
    postorder(t.left, proc)
    postorder(t.right, proc)
    proc(t.data)


def levelorder(t, proc):
    """宽度优先 使用队列"""
    q = SQueue()
    q.put(t)
    while not q.is_empty():
        t = q.get()
        if t is None:  # 树为空直接跳过
            continue
        q.put(t.left)
        q.put(t.right)
        proc(t.data)


def preorder_nonrec(t, proc):
    """
    遇到结点就访问，然后沿着左子树向下，同时右子树结点入栈
    遇到空树（叶结点）回溯，从栈中取出一个右分支，遍历
    """
    s = SStack()
    while t or not s.is_empty():
        while t:  # go down along left chain
            s.push(t.right)   # push right branch into stack
            proc(t.data)
            t = t.left
        t = s.pop()           # left chain ends, backtrack


def inorder_nonrec(t, proc):
    """深度优先 使用栈 中根LDR"""
    s = SStack()
    while t or not s.is_empty():
        while t:
            s.push(t)
            t = t.left
        t = s.pop()
        proc(t.data)
        t = t.right


def postorder_nonrec(t, proc):
    """深度优先 使用栈 后根LRD"""
    s = SStack()
    while t or not s.is_empty():
        while t:  # iterate until top has no child
            s.push(t)
            t = t.left if t.left else t.right
            # if we can go left, go, otherwise, go right
        # 到达叶结点
        t = s.pop()  # get the node to be access
        proc(t.data)
        if not s.is_empty() and s.top().left == t:
            t = s.top().right  # end of left visit, turn right
        else:
            t = None  # end of right visit, force to backtrack


def print_BinTNodes(t):
    if t is None:
        print("^", end="")
        return
    print("(" + str(t.data), end="")
    print_BinTNodes(t.left)
    print_BinTNodes(t.right)
    print(")", end="")


def preorder_elements(t):
    """生成器"""
    s = SStack()
    while t or not s.is_empty():
        while t:
            s.push(t.right)
            yield t.data
            t = t.left
        t = s.pop()


class BinTree:
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def set_root(self, rootnode):
        self._root = rootnode

    def set_left(self, leftchild):
        self._root.left = leftchild

    def set_right(self, rightchild):
        self._root.right = rightchild

    def root(self):
        return self._root

    def leftchild(self):
        return self._root.left

    def rightchild(self):
        return self._root.right

    def preorder_elements(self):
        t, s = self._root, SStack()
        while t or not s.is_empty():
            while t:
                s.push(t.right)
                yield t.data
                t = t.left
            t = s.pop()


if __name__ == "__main__":
    t1 = BinTNode(1, BinTNode(2, BinTNode(3), BinTNode(4)), BinTNode(5))
    print_BinTNodes(t1)
    print()

    preorder(t1, lambda x: print(x, end=" "))
    print()

    preorder_nonrec(t1, lambda x: print(x, end=" "))
    print()

    inorder(t1, lambda x: print(x, end=" "))
    print()

    inorder_nonrec(t1, lambda x: print(x, end=" "))
    print()

    postorder(t1, lambda x: print(x, end=" "))
    print()

    postorder_nonrec(t1, lambda x: print(x, end=" "))
    print()

    for x in preorder_elements(t1):
        print(x)
