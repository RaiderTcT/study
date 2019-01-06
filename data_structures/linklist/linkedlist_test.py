from linkedlist import LNode, LList
import unittest


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = LList()

    def tearDown(self):
        pass

    def test_init(self):
        self.assertEqual(self.ll._head, None)
        ln = LNode(1)
        self.ll = LList(ln)
        self.assertEqual(self.ll._head.elem, 1)

    def test_is_empty(self):
        self.assertEqual(True, self.ll.is_empty())
        ln = LNode(21)
        self.ll = LList(ln)
        self.assertEqual(False, self.ll.is_empty())

    def test_prepend(self):
        self.ll.prepend(1)
        self.assertEqual(1, self.ll._head.elem)
        self.ll.prepend(2)
        self.assertEqual(2, self.ll._head.elem)
        self.assertEqual(2, self.ll.count)

    def test_append(self):
        self.ll.append(1)
        p = self.ll._head
        while p.next is not None:
            p = p.next
        self.assertEqual(1, p.elem)
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        p = self.ll._head
        while p.next is not None:
            p = p.next
        self.assertEqual(3, p.elem)

    def test_pop_first(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        # 浅 拷贝
        p = self.ll._head
        self.assertEqual(1, p.elem)
        e = self.ll.pop_first()
        p = self.ll._head
        self.assertEqual(1, e)
        self.assertEqual(2, p.elem)

    def test_pop_last(self):
        for i in range(10):
            self.ll.append(i)
        e = self.ll.pop_last()
        self.assertEqual(9, e)
        p = self.ll._head
        while p.next:
            p = p.next
        self.assertEqual(8, p.elem)

    def test_print(self):
        for i in range(10):
            self.ll.append(i)
        self.ll.printall()

    def test_find(self):
        for i in range(10):
            self.ll.append(i)
        e = self.ll.find(lambda x: x if x>5 else None)
        self.assertEqual(6, e)

    def test_search(self):
        for i in range(10):
            self.ll.append(i)
        self.ll.for_search(print)
        # self.ll.printall()
        # p = self.ll._head
        # for i in range(10):
        #     self.assertEqual(i**2, p.elem)
            # p = p.next

if __name__ == '__main__':
    unittest.main()
