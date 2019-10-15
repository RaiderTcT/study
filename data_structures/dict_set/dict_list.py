#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Ulysses
@Date: 2019-10-15 08:29:11
@Description: 字典线性表的实现
@LastEditTime: 2019-10-15 16:49:32
'''
from data_structures.dict_set import Assoc

NOT_FOUND = object()
class NotFound:
    def __str__(self):
        return "not found"


class DictList:
    """
    基于顺序表实现
    平均检索长度ASL = 1*p0 + 2*p1 + ... + n*pn-1 = 1/n(1+2+..+n) = (n+1)/2 = O(n)
    假定检索概率相同
    检索和删除的效率较低
    """
    def __init__(self):
        self._elems = []

    def is_empty(self):
        """是否为空"""
        return not self._elems

    def nums(self):
        """获知元素个数"""
        return len(self._elems)

    def search(self, key):
        """检索与key关联的数据"""
        for e in self._elems:
            if e.key == key:
                return e.value
        return NotFound()

    def insert(self, key, value):
        """将关联(key,value)加入字典表, key已经存在则更新数据"""
        # for e in self._elems:
        #     if e.key == key:
        #         e.value = value
        #         return
        self._elems.append(Assoc(key, value))

    def delete(self, key):
        for i in range(len(self._elems)):
            if self._elems[i].key == key:
                self._elems.pop(i)
                return

    def values(self):
        """迭代字典中关联的value"""
        for a in self._elems:
            yield a.value

    def __iter__(self):
        """迭代(key, value)"""
        for e in self._elems:
            yield e.key, e.value

class DictOrdList(DictList):
    """
    基于有序表
    检索: O(logn)
    删除插入: O(n)
    """
    def search(self, key):
        """有序序列可以使用二分查找降低复杂度"""
        elems = self._elems
        low, high = 0, len(elems) - 1
        while low <= high:
            mid = (high-low) // 2
            if key == elems[mid].key:
                return elems[mid].value
            if key < elems[mid].key:
                high = mid - 1
            else:
                low = mid + 1
        return NotFound()

    def insert(self, key, value):
        """二分 插入排序"""
        if not self._elems:
            self._elems.append(Assoc(key, value))
        else:
            elems = self._elems
            elem = Assoc(key, value)
            length = len(elems)
            low, high, mid = 0, length - 1, -1
            # 确定插入的位置
            while low <= high:
                mid = (low + high) // 2
                if key == elems[mid].key:
                    # 替换
                    elems[mid].value = value
                    return
                if key > elems[mid].key:
                    low = mid + 1
                else:
                    high = mid - 1
            elems.append(None)
            for i in range(low, length+1):
                elems[i] = elems[i-1]
            elems[low] = elem

    def delete(self, key):
        if not self._elems:
            return NotFound()
        elems = self._elems
        length = len(elems)
        low, high, mid = 0, length - 1, -1
        while low <= high:
            mid = (low + high) // 2
            if elems[mid].key == key:
                break
            if key < elems[mid].key:
                high = mid - 1
            else:
                low = mid + 1
        if low <= high:
            for i in range(mid, length-1):
                elems[i] = elems[i+1]
            elems.pop()
            # elems.pop(mid)
            return value
        return NotFound()

if __name__ == "__main__":
    # dl = DictList()
    # print(dl.is_empty())
    # for i in range(10):
    #     dl.insert(chr(ord('a')+i), i)
    # for value in dl.values():
    #     print(value, end=', ')
    # print()
    # dl.insert('a', 101)
    # dl.insert('z', 111)
    # for key, value in dl:
    #     print(key, value, end=', ')
    # print()
    # print(dl.nums())
    # dl.delete('a')
    # dl.delete('x')
    # print(dl.nums())
    # print(dl.search('x'))

    dol = DictOrdList()
    for i in range(10, -1, -1):
        e = (chr(ord('z')-i), i)
        print(e, end=', ')
        dol.insert(*e)
    print()
    for key, value in dol:
        print(key, value, end=', ')
    print()

    print(dol.nums())
    dol.delete('s')
    print(dol.nums())
    for key, value in dol:
        print(key, value, end=', ')
    print()
    dol.delete('alll')
    print(dol.nums())
    for key, value in dol:
        print(key, value, end=', ')
    print()
