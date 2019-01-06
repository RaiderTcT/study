"""链表
"""


class LinkedListUnderflow(ValueError):
    pass


# 结点
class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LList:
    def __init__(self, node=None):
        self.count = 0
        if node:
            self._head = node
            self.count += 1
        else:
            self._head = None

    def is_empty(self):
        return self._head is None

    # 在最前端插入
    def prepend(self, elem):
        self._head = LNode(elem, self._head)
        self.count += 1

    # 在尾端插入
    def append(self, elem):

        self.count += 1
        # 若为空表
        if self._head is None:
            self._head = LNode(elem)
            return
        # 遍历到链表尾
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    # 最前端的数据出栈
    def pop_first(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop_first')
        self.count -= 1
        e = self._head.elem
        self._head = self._head.next
        return e

    # 尾端数据出栈
    def pop_last(self):
        if self._head is None:
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
        return e

    # 打印所有元素
    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
            # 还有后续节点 则以‘,’分隔继续输出
            if p.next is not None:
                print(', ', end='')
            p = p.next
        print('')

    # 传入判断谓词
    def find(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next

    # 遍历，传入操作参数
    def for_search(self, proc):
        p = self._head
        while p is not None:
            proc(p.elem)
            p = p.next

    # 迭代操作， 生成器方法
    def elements(self):
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    # 筛选出满足要求的所有数据，返回到一个generator中
    def filter(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next

    # 清除链表
    def clear(self):
        self._head = None

    # 指定位置插入
    def insert(self, i, elem):
        p = self._head

        if i == 0:
            self.prepend(elem)
        elif i >= self.count:
            self.append(elem)
        else:
            j = 0
            self.count += 1
            while j < i:
                p = p.next
                j += 1
            q = LNode(elem, p.next)
            p.next = q

    # 指定移除
    def remove(self, i):
        p = self._head
        if i == 0:
            self._head = self._head.next
        else:
            if i >= self.count:
                raise ValueError('x is not in LinkedList')
            else:
                j = 0
                while j < i:
                    p = p.next
                    j += 1
                p.next = p.next.next

    def reverse(self):
        """
        反转， 从表首开始取节点，插入另一个链表的首端 O(n)
        """
        p = None
        while self._head is not None:
            q = self._head
            self._head = q.next
            q.next = p
            p = q
        self._head = p

    def sort_1(self):
        """
        插入法， 移动表中元素
                 x
        1234678  5
        1234578  6
        1234568  7
        1234567  8
        """
        if self._head is None:
            return
        crt = self._head.next
        while crt:
            x = crt.elem
            p = self._head
            while p is not crt and p.elem <= x:
                p = p.next
            while p is not crt:  # 找到crt插入的位置
                p.elem, x = x, p.elem  # 将crt元素插入该位置
                p = p.next
            crt.elem = x  # 回填最后一个元素
            crt = crt.next

    def sort_2(self):
        p = self._head
        if p is None or p.next is None:
            return

        rem = p.next  # 除head之外的节点段
        p.next = None
        while rem is not None:
            p = self._head
            q = None
            while p is not None and p.elem < rem.elem:
                q = p
                p = p.next
            if q is None:
                self._head = rem
            else:
                q.next = rem
            q = rem
            rem = rem.next
            q.next = p


if __name__ == "__main__":
    import random
    l1 = LList()
    for i in range(1, 10):
        l1.append(random.randint(1, 100))
    l1.printall()
    l1.reverse()
    l1.printall()
    l1.sort_2()
    l1.printall()
