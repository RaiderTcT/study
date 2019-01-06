"""
Josephus问题： n个人围坐一圈，
从第k个人开始报数， 报到第m个数的人退出，
然后下一个人开始继续报数并按同样的规则退出，直到所有人退出
"""
from linked_circular_list import LCList


def josephus_A(n, k, m):
    people = list(range(1, n+1))

    i = k - 1
    for num in range(n):
        count = 0
        while count < m:
            if people[i] > 0:
                count += 1
            if count == m:
                print(people[i], end="")
                people[i] = 0
            i = (i + 1) % n
        if num < n - 1:
            print(', ', end="")
        else:
            print("")
    return


def josephus_L(n, k, m):
    """
    基于顺序表的解， 确定退出的人员后，将其从列表中删除pop
    """
    people = list(range(1, n + 1))
    num, i = n, k - 1
    for num in range(n, 0, -1):
        i = (i + m - 1) % num
        print(people.pop(i), end=", " if num > 1 else "\n")
    return


class Josephus(LCList):
    """基于循环单链表的解，退出的人员 删除其节点
    """
    def turn(self, m):
        """将尾指针rear向后移m步"""
        for _ in range(m):
            self._rear = self._rear.next

    def __init__(self, n, k, m):
        super().__init__()
        for i in range(n):
            self.append(i + 1)
        self.turn(k-1)  # 移动rear，相当于将head指向第k个人
        while not self.is_empty():
            self.turn(m-1)
            print(self.pop(), end='\n' if self.is_empty() else ', ')


if __name__ == "__main__":
    josephus_A(10, 2, 5)
    josephus_L(10, 2, 5)
    Josephus(10, 2, 5)
