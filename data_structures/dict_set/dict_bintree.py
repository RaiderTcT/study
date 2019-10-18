#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Ulysses
@Date: 2019-10-18 14:23:56
@Description:  基于二叉树的字典实现
@LastEditTime: 2019-10-18 17:32:04
'''
from data_structures.dict_set import Assoc
from data_structures.tree.binary_tree import BinTreeNode
from data_structures.stack_queue.stack import SStack


# 二叉排序树:  左子树< 根 <右子树; 中根遍历 -> 递归序列
def bt_serach(tree, key):
    """二叉排序树检索"""
    bt = tree
    while bt is not None:  # left data right
        entry = bt.data
        if key > entry.key:  # 向右子树查找
            bt = bt.right
        elif key < entry.key:
            bt = bt.left
        else:
            # 检索到key 返回对应value
            return entry.value
    return None


class DictBinTree:
    def __init__(self):
        self._root = None

    def serarch(self, key):
        bt = self._root
        while bt is not None:  # left data right
            entry = bt.data
            if key > entry.key:  # 向右子树查找
                bt = bt.right
            elif key < entry.key:
                bt = bt.left
            else:
                # 检索到key 返回对应value
                return entry.value
        return None

    def insert(self, key, value):
        bt = self._root
        if bt is None:
            # 空二叉树 建立新的root节点
            self._root = BinTreeNode(Assoc(key, value))
            return
        while True:
            entry = bt.data
            if key < entry.key:  # 向左子树查询
                if bt.left is None:  # 左右子树为空 找到要插入的位置
                    bt.left = BinTreeNode(Assoc(key, value))
                    return
                # 非空则 继续向下查找
                bt = bt.left
            elif key > entry.key:
                if bt.right is None:
                    bt.right = BinTreeNode(Assoc(key, value))
                    return
                bt = bt.right
            else:
                # 更新value
                bt.data.value = value
                return

    def values(self):
        """中序迭代 节点的value"""
        t, st = self._root, SStack()
        while t is not None or not st.is_empty():
            # 不断向下将左子节点入栈
            while t is not None:
                st.push(t)
                t = t.left
            # 到底部
            t = st.pop()
            yield t.data.value
            # 左子节点处理完后 从最底部右子节点开始处理
            t = t.right

    def __iter__(self):
        """中序遍历 深度优先 LDR"""
        t, st = self._root, SStack()
        while t is not None or not st.is_empty():
            # 不断向下将左子节点入栈
            while t is not None:
                st.push(t)
                t = t.left
            # 到底部
            t = st.pop()
            # Assoc对象不让外界获取到,防止字典表完整性被破换
            yield t.data.key, t.data.value
            # 左子节点处理完后 从最底部右子节点开始处理
            t = t.right

    def delete(self, key):
        """
        删除: 1. 要删除的节点q是叶节点, 则只需要将其父节点p与q引用设置为None
        2. q是分支节点, 要将q的子树连接到删除q后的树中, 设q为p的左子树(
            右子树的情况类似):
        ① q没有左子节点, 将q的右子树替换q作为p的左子树
        ② q有左子节点, 取q左子树最右边节点r(它没有右子树).用q的左子节点代替q,
        q的右字节作为r的右子树
        """
        p, q = None, self._root
        while q is not None and q.data.key != key:
            p = q  # 维持p为q的父节点
            if key < q.data.key:
                q = q.left
            else:
                q = q.right
            if q is None:
                # 没有找到key对应的节点
                return
        # 删除q引用的节点, p为其父节点或None(q为root)

        # q没有左子树
        if q.left is None:  # q右子树代替q即可
            if p is None:  # 要删除的是根节点
                self._root = q.right
            elif q is p.left:  # 根据p和q的关系,修改p的左子树或右子树
                p.left = q.right
            else:
                p.right = q.right
            return

        # q 有左子节点
        r = q.left
        # 先找到q左子树下面最右边的节点
        while r.right is not None:
            r = r.right

        r.right = q.right
        if p is None:
            self._root = q.left
        elif q is p.left:
            p.left = q.left
        else:
            p.right = q.left

    def print(self):
        for entry in self:
            print(entry, end=', ')
        print()

if __name__ == "__main__":
    import random
    l1 = [random.randint(1, 100) for _ in range(10)]
    l2 = [chr(ord('a') + i) for i in range(10)]
    d = list(zip(l1, l2))
    print(d)
    dt = DictBinTree()
    for key, value in d:
        dt.insert(key, value)
    for value in dt.values():
        print(value, end=', ')
    print()
    dt.print()

    delete_num_1 = d[0]
    print("删除root: ", delete_num_1)
    dt.delete(delete_num_1[0])
    dt.print()

    delete_num_2 = d[5]
    print("删除: ", delete_num_2)
    dt.delete(delete_num_2[0])
    dt.print()
