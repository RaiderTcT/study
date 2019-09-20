""" 优先队列的两个实现：连续表实现和堆实现 """

# This file contains two
# implementations of priority queues:
# 1, as sorted list
# 2, as heap stored in a list
# and in addition,
# an implementation of heap sort function

from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)  # 生成__eq__(), __lt__()等方法
class PriorityItem:
    priority: int
    item: Any = field(compare=False)  # 此项不会进行比较


class PrioQueueError(ValueError):
    pass


class PrioQue:
    """ Implementing binary trees as sorted list
    """
    def __init__(self, elist=[]):
        self._elems = list(elist)
        self._elems.sort(reverse=True)  # 较小的值 优先级高， 在表尾

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError("in top")
        return self._elems[-1]

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError("in pop")
        return self._elems.pop()

    def enqueue(self, e):  # 只有插入时是O(n)(线性结构)操作，其他O(1)
        i = len(self._elems) - 1
        while i >= 0:
            if self._elems[i] <= e:
                i -= 1
            else:
                break
        self._elems.insert(i+1, e)

    def show(self):  # only for test
        print(",".join(map(str, self._elems)))


# 堆 使用树形结构实现的优先队列，结点里存储数据的 完全二叉树
# 内置heap：从零开始计数，对于所有的k，都有
# heap[k] <= heap[2*k+1]和 heap[k] <= heap[2*k+2]（小顶堆）
# 任一结点里所存的数据先于或等于其子结点里的数据（序）
# 不同路径上的元素，不关心其顺序
# 一颗完全二叉树可以自然而且完全地存入一个连续的线性结构 把堆看作原生的Python list
class PrioQueue:
    """ Implementing priority queues using heaps
    """
    def __init__(self, elist=[]):
        self._elems = list(elist)
        if elist:
            self.buildheap()

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError("in peek")
        return self._elems[0]

    def enqueue(self, e):
        self._elems.append(None)  # add a dummy element
        self.siftup(e, len(self._elems)-1)

    def siftup(self, e, last):
        """
        向上筛选
        要插入的值与堆中元素进行比较确定插入位置
        Args:
            e (Any): 插入的值
            last (int): 最后一个元素下标
        """
        elems, i, j = self._elems, last, (last-1)//2
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j-1)//2
        elems[i] = e

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError("in dequeue")
        elems = self._elems
        e0 = elems[0]  # 取堆顶最优先的元素
        e = elems.pop()  # 取尾部元素 重新构造一个完整堆
        if len(elems) > 0:
            self.siftdown(e, 0, len(elems))
        return e0

    def siftdown(self, e, begin, end):
        elems, i, j = self._elems, begin, begin*2+1
        while j < end:    # invariant: j == 2*i+1
            if j+1 < end and elems[j+1] < elems[j]:
                j += 1    # elems[j] <= its brother
            if e < elems[j]:     # e is the smallest of the three
                break
            elems[i] = elems[j]  # elems[j] is the smallest, move it up
            i, j = j, 2*j+1
        elems[i] = e

    def buildheap(self):
        # O(n)
        end = len(self._elems)
        for i in range(end//2, -1, -1):  # 从最下最右的分支节点开始
            # 向左建堆，再向上一层建堆
            self.siftdown(self._elems[i], i, end)


def heap_sort(elems):
    def siftdown(elems, e, begin, end):
        """构造大顶堆"""
        i, j = begin, begin*2+1
        while j < end:  # invariant: j == 2*i+1
            if j+1 < end and elems[j+1] > elems[j]:
                j += 1  # elems[j] >= its brother
            if e > elems[j]:     # e is the biggest of the three
                break
            elems[i] = elems[j]  # elems[j] is the smallest, move it up
            i, j = j, 2*j+1
        elems[i] = e

    end = len(elems)
    for i in range(end//2, -1, -1):
        siftdown(elems, elems[i], i, end)
    # O(nlogn) 逐个取堆顶后，将其放在尾部，重新构造堆，再取堆顶
    for i in range((end-1), 0, -1):
        e = elems[i]
        elems[i] = elems[0]
        siftdown(elems, e, 0, i)


from random import randint


def test1():
    print("Test class PrioQue:")
    pq = PrioQue([11, 22, 33])
    pq.show()
    for i in range(12):
        pq.enqueue(randint(0, 30))
    pq.show()
##    while not pq.is_empty():
##        print(pq.dequeue())


def test2():
    print("Test class PrioQueue:")
    pq = PrioQueue([1, 2, 3])
    for i in range(12):
        pq.enqueue(randint(0, 30))
    while not pq.is_empty():
        print(pq.dequeue())


def test3():
    print("Test function heap_sort:")
    lst = [randint(i, 30) for i in range(15)]
    print(lst)
    heap_sort(lst)
    print(lst)

if __name__ == '__main__':
    test1()

    test2()

    test3()

    pass
