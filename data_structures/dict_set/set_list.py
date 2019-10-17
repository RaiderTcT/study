#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Ulysses
@Date: 2019-10-17 08:32:46
@Description: 基于线性表的集合实现
@LastEditTime: 2019-10-17 14:21:21
'''
class LSet:
    """简单线性表实现"""
    def __init__(self, elems=[]):
        self._elems = []
        for x in elems:
            if x not in self._elems:
                self._elems.append(x)

    def __contains__(self, e):
        return e in self._elems

    def __iter__(self):
        yield from self._elems

    def __str__(self):
        return f"{self._elems}"

    def union(self, other):
        """并集"""
        elems = self._elems[:]
        for e in other:
            if e not in elems:
                elems.append(e)
        return elems

    def intersection(self, other):
        """交集 复杂度 O(m*n)"""
        e = []
        for elem in other:
            if elem in self._elems:
                e.append(elem)
        return e

    def difference(self, other):
        """差集"""
        elems = []
        for e in self._elems:
            if e not in other:
                elems.append(e)
        return elems

    def __or__(self, other):
        return self.union(other)

    def __sub__(self, other):
        return self.difference(other)

    def __and__(self, other):
        return self.intersection(other)

class LSet1(LSet):
    """简单线性表实现"""
    def add(self, e):
        if not e in self._elems:
            self._elems.append(e)
            return True
        return False

    def remove(self, e):
        for i in range(len(self._elems)):
            if self._elems[i] == e:
                self._elems.pop(i)
                return True
        return False


class LSet2(LSet):
    def add(self, e):
        self._elems.append(e)

    def remove(self, e):
        while e in self._elems:
            self._elems.remove(e)


class SortedListSet(LSet):
    # 基于排序表的set
    def __init__(self, elems=[]):
        sorted_elems = sorted(elems)
        self._elems = []
        for e in sorted_elems:
            if e not in self._elems:
                self._elems.append(e)

    def binary_search(self, e):
        """二分找到e的位置"""
        elems = self._elems
        low, high, mid = 0, len(elems) - 1, -1
        while low <= high:
            mid = (low + high) // 2
            if e == elems[mid]:
                # 已存在e
                break
            if e < elems[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low, mid, high

    def add(self, e):
        low, _, high = self.binary_search(e)
        if low <= high:
            # 找到了e 不需要添加
            return False
        else:
            ori_len = len(self._elems)
            self._elems.append(None)
            for i in range(low, ori_len):
                self._elems[i+1] = self._elems[i]
            self._elems[low] = e
            return True

    def remove(self, e):
        low, mid, high = self.binary_search(e)
        if low <= high:
            # 找到了e 删除
            for i in range(mid, len(self._elems)-1):
                self._elems[i] = self._elems[i+1]
            self._elems.pop()
            return True
        else:
            # 没有e
            return False

    def intersection(self, other):
        # 复杂度 O(m+n)
        inter = SortedListSet()  # 交集
        elems = self._elems
        other = other._elems
        i, j = 0, 0  # 两个集合下一次检查的坐标
        while i < len(elems) and j < len(other):
            # A当前元素小于B当前元素, A当前元素必定不在交集中
            if elems[i] < other[j]:
                i += 1
            elif elems[i] > other[j]:
                j += 1
            else:  # 取相同元素
                inter._elems.append(elems[i])
                i += 1
                j += 1
        return inter

    def union(self, other):
        union = SortedListSet()
        elems = self._elems
        other = other._elems
        i, j = 0, 0
        while i < len(elems) and j < len(other):
            if elems[i] < other[j]:
                union._elems.append(elems[i])
                i += 1
            elif elems[i] > other[j]:
                union._elems.append(other[j])
                j += 1
            else:  # 取相同元素
                union._elems.append(elems[i])
                i += 1
                j += 1
        # 添加另一个集合剩下的元素
        if i == len(elems) and j < len(other):
            union._elems.extend(other[j:])
        if j == len(other) and i < len(elems):
            union._elems.extend(elems[:])
        return union

    def difference(self, other):
        """差集"""
        diff = SortedListSet()
        elems = self._elems
        other = other._elems
        i, j = 0, 0
        while i < len(elems) and j < len(other):
            # A当前元素<B当前元素, 当前A元素不在交集中
            if elems[i] < other[j]:
                diff._elems.append(elems[i])
                i += 1
            elif elems[i] > other[j]:
                j += 1
            else:
                i += 1
                j += 1
        # 取剩余元素
        if i < len(elems):
            diff._elems.extend(elems[i:])
        return diff


if __name__ == "__main__":
    set2 = LSet2(list(range(5)))
    set2.add(2)
    print(set2)
    set2.remove(2)
    print(set2)
    print(2 in set2, 1 in set2)

    set1 = LSet1([1, 2 ,2,4, 5, 7])
    print("set1: ", set1)
    set1.add(2)
    print("set1: ", set1)
    set1.remove(2)
    print("set1: ", set1)

    print("差集: ", set1 - set2)
    print("并集: ", set1 | set2)
    print("交集: ", set1 & set2)

    set3 = SortedListSet([8, 4, 1, 2, 1, 2, 5, 3])
    print("set3: ", set3)
    set3.add(6)
    print("set3: ", set3)
    set3.remove(4)
    print("set3: ", set3)
    set4 = SortedListSet([1, 3 , 5, 7, 9])
    print("set4: ", set4)
    print("差集: ", set3 - set4)
    print("交集: ", set3 & set4)
    print("并集: ", set3 | set4)
