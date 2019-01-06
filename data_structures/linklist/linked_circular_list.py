class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LCList:
    """循环单链表，最后一个节点的next不指向None，指向链表的头
    """
    def __init__(self):
        # 记录表尾节点
        self._rear = None

    def is_empty(self):
        return self._rear is None

    # 在表头前插入
    def prepend(self, elem):
        p = LNode(elem)
        # 空表 建立一个节点的环
        if self._rear is None:
            self._rear = p
            p.next = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    # 在表尾插入,在最前端插入结点，尾指针指向新结点
    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next

    # 弹出最前端
    def pop(self):
        if self._rear is None:
            raise ValueError('in pop of CLList')
        else:
            p = self._rear.next
            # 只有一个结点
            if self._rear is p:
                self._rear = None
            else:
                # 多于1个结点，指向下一个结点
                self._rear.next = p.next
        return p.elem

    # 输出表元素
    def printall(self):
        if self.is_empty():
            return
        else:
            # 从头开始打印
            p = self._rear.next
            while True:
                print(p.elem, end=' ')
                # 当到达最尾端
                if p is self._rear:
                    break
                p = p.next
            print('')


if __name__ == "__main__":
    lcl = LCList()
    for i in range(10):
        lcl.append(i)
    lcl.printall()
    lcl.pop()
    print('------------')
    lcl.printall()
    print('------------')
    lcl.prepend(123)
    lcl.printall()
