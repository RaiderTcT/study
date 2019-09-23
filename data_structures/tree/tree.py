#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Ulysses
@Date: 2019-09-23 10:05:20
@Description: 使用list来实现树tree, Tree类
@LastEditTime: 2019-09-23 19:45:01
'''
# 树结点由2部分组成：结点本身数据以及一组子树


class SubtreeIndexError(ValueError):
    pass


def tree(data, *subtrees):
    """使用python的list嵌套结构"""
    l = [data]
    l.extend(subtrees)
    return l


def is_empty_Tree(tree):
    return tree is None


def subtree(tree, i):
    """获取第i棵子树"""
    if i < 1 or i > len(tree):
        raise SubtreeIndexError
    return tree[i + 1]


def root(tree):
    return tree[0]


def set_root(tree, data):
    tree[0] = data


def set_subtree(tree, i, subtree):
    if i < 1 or i > len(tree):
        raise SubtreeIndexError
    tree[i + 1] = subtree


class TreeNode:
    def __init__(self, data, subs=[]):
        self._data = data
        self._subtrees = list(subs)

    def __str__(self):
        return f"[TreeNode {self._data} {self._subtrees}]"


class Tree:
    def __init__(self, data, subs=[]):
        self._root = TreeNode(data, subs)

    def root(self):
        if self._root is not None:
            return self._root._data
        return None

    def set_root(self, data):
        self._root._data = data

    def is_empty(self):
        return self._root is None

    def add_subtree(self, subs=[]):
        if not self.is_empty():
            self._root._subtrees.extend(subs)

    def get_subtree(self, i):
        if not self.is_empty():
            if i < 1 or i > len(self._root._subtrees):
                raise SubtreeIndexError
            return self._root._subtrees[i]

    def set_subtree(self, i, tree):
        if not self.is_empty():
            if i < 1 or i > len(self._root._subtrees):
                raise SubtreeIndexError
            self._root._subtrees[i] = tree

    def traversal(self):
        print(self._root._data)
        for data in self._root._subtrees:
            print(data)


if __name__ == "__main__":
    tree1 = tree('+', 1, 2, 3)
    tree2 = tree('*', 2, 4, 6)
    set_subtree(tree1, 2, tree2)
    print(tree1)
    print(tree2)

    t1 = Tree(1)
    t2 = TreeNode(2, [1, 3, 5])
    t3 = TreeNode(3, [4, 7])
    t1.add_subtree([t2, t3])
    t1.traversal()
