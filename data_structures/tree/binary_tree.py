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
    """深度优先 使用栈 先根"""
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
