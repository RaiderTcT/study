#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 二叉树
@Date: 2019-09-18 20:55:09
@Author: Ulysses
@LastEditTime: 2019-09-18 21:07:07
'''


class BinaryTree:
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

if __name__ == "__main__":
    bt1 = BinaryTree(
        2, BinaryTree(4, BinaryTree(3), BinaryTree(6)),
        BinaryTree(8, BinaryTree(9), BinaryTree(12))
    )
    print(bt1.left_child().right_child())
