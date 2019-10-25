#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Ulysses
@Date: 2019-10-25 15:03:33
@Description: 30 seconds of python List
@LastEditTime: 2019-10-25 17:32:39
'''

def all_equal(lst):
    """
    序列中所有元素是否相等
    l[1], l[2], l[3], ..., l[n-1]
    l[0], l[1], l[2], ..., l[n-2]
    """
    return lst[1:] == lst[:-1]

def all_unique(lst):
    """序列中所有的元素都是唯一的"""
    return len(lst) == len(set(lst))


def bifurcate(lst, filter):
    """根据filter中bool值对lst进行分组"""
    return [
        [x for i, x in enumerate(lst) if filter[i] == True],
        [x for i, x in enumerate(lst) if filter[i] == False],
    ]


def bifurcate_by(lst, f):
    """根据函数f对lst中的元素进行划分"""
    return [
        [x for x in lst if f(x)],
        [x for x in lst if not f(x)],
    ]

def chunk(lst, size):
    """
    将lst分割成size大小的子块
    """
    from math import ceil
    # ceil(x) 大于x值的最小整数
    return list(map(
        lambda x: lst[x * size:x * size + size],
        list(range(0, ceil(len(lst) / size)))  # [0, 1]
    ))

print("chunk", chunk([1, 2, 3, 4, 5, 6, 7], 3))
# [[1, 2, 3], [4, 5, 6], [7]]

def compact(lst):
    """
    使用filter取出lst中的falsey数据(None, 0, ''和False)
    bool(lst[i])
    """
    return list(filter(bool, lst))

def count_by(lst, fn=lambda x:x):
    """
    根据给定函数,将lst元素分组,并返回各组的元素数量
    """
    key = {}
    for result in map(fn, lst):
        key[result] = 1 if result not in key else key[result] + 1
    return key

print("count_by", count_by(['111', '22', 'three', 'one'], len))
# {3: 2, 2: 1, 5: 1}

def count_occorences(lst, value):
    """
    计算lst中某一值出现的次数
    """
    return len([x for x in lst if x == value and type(x) == type(value)])

print("count_occorences", count_occorences([1, 2, 3, 1, 2, 1], 1))
# count_occorences 3

def deep_flatten(lst):
    """扁平化嵌套的可迭代对象"""
    from collections.abc import Iterable
    for e in lst:
        if isinstance(e, Iterable):
            yield from deep_flatten(e)
        else:
            yield e

print("deep_flatten", list(deep_flatten([1, [1, 2, 4, [100, 111]], 5, [8, 9]])))
# deep_flatten [1, 1, 2, 4, 100, 111, 5, 8, 9]

def difference(a, b):
    """
    返回两个可迭代对象的差异
    """
    _b = set(b)
    return [item for item in a if item not in _b]

def difference_by(a, b, fn):
    """
    根据fn函数的结果 返回差异
    """
    _b = set(map(fn, b))
    return [item for item in a if fn(item) not in _b]

from math import floor

print("difference_by", difference_by([1.1, 2.1, 3.7, 5], [2.2, 3.1], floor))
# difference_by [1.1, 5]

def every(lst, fn=lambda x: x):
    """
    lst所有元素执行fn都为True则返回True, 否则返回False
    """
    # all 所有对象bool()都为True
    return all(map(fn, lst))

def every_nth(lst, nth):
    """
    lst每隔nth取一个元素,构成一个新序列
    """
    return lst[nth-1::nth]

print("every_nth", every_nth(list(range(10)), 3))
# every_nth [2, 5, 8]

def filter_non_unique(lst):
    """
    过滤出lst中出现不止一次的元素, 剩出现一次的
    """
    return [item for item in lst if lst.count(item) == 1]

print("filter_non_unique", filter_non_unique([1, 2, 2, 4, 3, 4, 6]))
# filter_non_unique [1, 3, 6]

def filter_unique(lst):
    return list(set(item for item in lst if lst.count(item) > 1))

print("filter_unique", filter_unique([1, 2, 2, 4, 3, 4, 6]))
# filter_unique [2, 4]

def flatten(lst):
    """二重列表打开"""
    # for y in lst:
    #     for x in y:

    return [x for y in lst for x in y]

print("flatten", flatten([[1, 2, 3], [4, 5, 6]]))
# flatten [1, 2, 3, 4, 5, 6]

def group_by(lst, fn):
    """根据函数fn执行结果对lst进行分组"""
    # d = {}
    # for key in map(fn, lst):
    #     d[key] = [e for e in lst if fn(e) == key]
    # return d
    return {key: [e for e in lst if fn(e) == key] for key in map(fn, lst)}

print("group_by", group_by([6.1, 6.2, 4.2, 3.1], floor))
# group_by {6: [6.1, 6.2], 4: [4.2], 3: [3.1]}

def has_duplicates(lst):
    """是否有重复的元素"""
    return len(lst) != len(set(lst))

def initial_2d_list(w, h, value=None):
    """初始化一个w*h的二维数组"""
    return [[value]*h for _ in range(w)]

print("initial_2d_list", initial_2d_list(3, 4, 0))
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
