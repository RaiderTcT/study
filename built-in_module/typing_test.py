#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Ulysses
@Date: 2019-09-12 11:30:20
@Description: 类型别名
@LastEditTime: 2020-04-03 09:43:48
'''
from typing import Any, List, NewType
from dataclasses import dataclass, field

Vector = List[float]  # Vector 和 List[float] 将被视为可互换的同义词

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

new_vector = scale(2.0, [1.0, 2.0, 3.0])
print(new_vector)

# 使用 NewType() 辅助函数创建不同的类型:
UserId = NewType('UserId', int)
some_id = UserId(134)
print(some_id)

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)

p1 = PrioritizedItem(1, 'a')
p2 = PrioritizedItem(2, 'z')
p3 = PrioritizedItem(2, [1, 2, 3])

print(p2 > p1)
print(p3 == p2)
