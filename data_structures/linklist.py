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


if __name__ == "__main__":
    ld = list((1,2,3,4,5))
    print(ld)
    ld.remove(4)
    print(ld)
    # 插入 2 3之间