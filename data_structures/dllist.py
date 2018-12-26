"""
双链表
"""
from linkedlist_1 import LList1, LinkedListUnderflow


class DLNode:
    """双链表节点， prev elem next"""
    def __init__(self, elem, prev=None, next=None):
        self.elem = elem
        self.prev = prev
        self.next = next


class DLList(LList1):
    def __init__(self):
        super().__init__()

    def append(self, elem):
        """尾端插入"""
        self.count += 1
        p = DLNode(elem, self._rear, None)
        if self._head is None:  # 空表插入
            self._head = p
        else:
            p.prev.next = p
        self._rear = p  # 更新尾域

    def prepend(self, elem):
        """首端插入"""
        self.count += 1
        p = DLNode(elem, None, self._head)
        if self._head is None:
            self._rear = p
        else:
            p.next.prev = p
        self._head = p

    def pop_first(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop_first')
        self.count -= 1
        e = self._head.elem
        self._head = self._head.next
        if self._head is not None:
            self._head.prev = None  # 链表第一个节点 prev 为None
        return e

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop_last')
        self.count -= 1
        e = self._rear.elem
        self._rear = self._rear.prev
        if self._rear is None:  # 只有一个节点，删除了为空
            self._head = None
        else:
            self._rear.next = None
        return e

    def reverse(self):
        if self._head is None:
            raise LinkedListUnderflow(" empty linked list")
        nodes = self.nodes()
        for node in nodes:
            node.prev, node.next = node.next, node.prev
        # self._head, self._rear = self._rear, self._head


if __name__ == "__main__":
    import random
    mlist1 = DLList()
    mlist1.append(1)
    mlist1.prepend(99)

    for i in range(10):
        mlist1.append(random.randint(1, 20))
    mlist1.printall()
    for x in mlist1.filter(lambda x: x % 2 == 0):
        print(x)
    print(mlist1.count)

    mlist1.reverse()
    mlist1.printall()
