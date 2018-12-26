"""
带尾节点引用的单链表
"""
from linkedlist import LList, LNode, LinkedListUnderflow


class LList1(LList):
    def __init__(self):
        super().__init__()
        self._rear = None

    def prepend(self, elem):
        self.count += 1
        if self._head is None:  # 空表 添加 尾=头
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)

    def append(self, elem):
        self.count += 1
        if self._head is None:  # 空表
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem, None)
            self._rear = self._rear.next

    def pop_last(self):
        if self._head is None:  # 没有节点
            raise LinkedListUnderflow('in pop_last')
        p = self._head
        self.count -= 1
        # 只有一个结点，修改表头指针
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        # 找到倒数第2个，将其next指向None
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e


if __name__ == "__main__":
    import random
    mlist1 = LList1()
    mlist1.append(1)
    mlist1.prepend(99)

    for i in range(10):
        mlist1.append(random.randint(1, 20))
    mlist1.printall()
    for x in mlist1.filter(lambda x: x % 2 == 0):
        print(x)
    print(mlist1.count)
