#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Ulysses
@Date: 2019-09-20 10:25:59
@Description: 哈弗曼树
@LastEditTime: 2019-09-20 14:16:48
'''
from data_structures.tree.binary_tree import print_BinTNodes
from data_structures.tree.binary_tree import BinTNode
from data_structures.tree.prioqueue import PrioQueue
from data_structures.stack_queue.stack import SStack
"""
带权扩充二叉树外部路径长度
WPL=∑ wi*li, wi是外部节点i的权
设有实数集 W={w0, w1, ..., wm-1}, T为一棵扩充二叉树，其m个外部结点分别以wi为权
而且T的带权外部路径长度WPL在所有这样的扩充二叉树中达到最小，则T为数据集W的
最优二叉树或哈弗曼树
算法：
- 输入为实数级 W={w0, w1, ..., wm-1}
- 在构造中维护这k棵二叉树的集合F，开始时k=m且F={T0, T1, ..., Tm-1}, 其中Ti
是一棵只包含权为wi的根结点的单点二叉树
- 构造时重复下面2步，直到集合F中只剩一棵树：
  1. 构造一棵新二叉树，其左右子树是从集合F中选取的两棵权最小二叉树，其根结点
  的权值设置为这2棵子树的根节点的权值之 和
  2. 将所选的2棵二叉树从F中删除，新构造的树加入F
实现：
构造一个优先队列存放F中的二叉树，按权值从小到大排序；
1）从队列中取2棵二叉树作为左右子树，他们的权值为最小，
2）构造新二叉树，根结点数值为子树权的和，然后加入优先队列中
"""
class HTNode(BinTNode):
    def __lt__(self, othernode):
        return self.data < othernode.data
    
    def __le__(self, othernode):
        return self.data <= othernode.data


class HuffmanPrioQ(PrioQueue):
    def number(self):
        return len(self._elems)


def HuffmanTree(weights):
    trees = HuffmanPrioQ()
    for w in weights:
        trees.enqueue(HTNode(w))
    while trees.number() > 1:
        t1 = trees.dequeue()
        t2 = trees.dequeue()
        x = t1.data + t2.data
        trees.enqueue(HTNode(x, t1, t2))
    return trees.dequeue()


def huffman_encode(str_dic):
    def get_leaves(t):
        s = SStack()
        encode_char = ''
        while t is not None or not s.is_empty():
            while t is not None:
                encode_char += t.encode_char
                character = t.character
                s.push((t.right, encode_char))
                t = t.left
                if t is None:
                    yield character, encode_char
                    encode_char = ''
            t, encode_char = s.pop()

    trees = HuffmanPrioQueue()
    for key, value in str_dic.items():
        trees.enqueue(HTNode(value, None, None, key, ''))
    while trees.number() > 1:
        t1 = trees.dequeue()
        t2 = trees.dequeue()
        t1.encode_char = '0'
        t2.encode_char = '1'
        x = t1.data + t2.data
        trees.enqueue(HTNode(x, t1, t2))
    yield from get_leaves(trees.dequeue())
 
  
if __name__ == '__main__':

    t = BinTNode(1, BinTNode(2), BinTNode(3))
    print_BinTNodes(t)
    print("\n")

    h = HuffmanTree([2, 3, 7, 10, 4, 2, 5])
    print_BinTNodes(h)
    print()
    temp_dict = {
        'a': 2,
        'b': 3,
        'c': 7,
        'd': 4,
        'e': 10,
        'f': 2,
        'h': 5
    }
    for char, encode_char in huffman_encode(temp_dict):
        print(f"{char}: {encode_char}")
    pass
