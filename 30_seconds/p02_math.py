#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Ulysses
@Date: 2019-10-28 08:12:32
@Description: math 相关
@LastEditTime: 2019-10-28 09:46:32
'''
import math
from functools import reduce


def average(*args):
    return sum(args, 0.0) / len(args)


print("average", average(*[1, 2, 3]))


def average_by(lst, fn=lambda x: x):
    """先执行fn后对结果求平均"""
    return sum(map(fn, lst), 0.0) / len(lst)

def clamp_number(num, a, b):
    """
    在a, b指定的范围内取最接近num值, 如果num在a,b范围内, 就取num
    """
    return max(min(a, b), min(max(a, b), num))


print("clamp_number", clamp_number(5, 1, 4))
print("clamp_number", clamp_number(3.5, 1, 4,))
print("clamp_number", clamp_number(0, 4, 1))


def degrees_to_rads(deg):
    """度->弧度"""
    return (deg * math.pi) / 180.0


def rads_to_degrees(rad):
    return (rad * 180.0) / math.pi


def digitize(num):
    """将num数字转为一个list包含每位数字"""
    return list(map(int, str(num)))


print("digitize", digitize(12345))


def factorial(num):
    """阶乘"""
    if not ((num >= 0) and (num % 1 == 0)):
        raise ValueError("需要一个正整数")
    return 1 if num == 0 else num * factorial(num - 1)


def fibonacci(n):
    """
    fibonacci序列 0 , 1, 1, 2, 3, 5
    """
    if n <= 0:
        return [0]
    seq = [0, 1]
    while len(seq) <= n:
        next_value = seq[len(seq) - 1] + seq[len(seq) - 2]
        seq.append(next_value)
    return seq


print("fibonacci", fibonacci(7))


def fibonacci_yield(n):
    a, b, count = 0, 1, 0
    while n > count:
        count += 1
        yield b
        a, b = b, a + b

print("fibonacci_yield")
for i in fibonacci_yield(7):
    print(i, end=', ')
print()


def gcd(numbers):
    """
    多个数的最大共约数
    """
    return reduce(math.gcd, numbers)


print("gcd", gcd([100, 220, 80]))
# gcd 20


def in_range(n, start, end=0):
    """n是否在(start, end)范围 默认从(0, start)
    """
    if (start > end):
        end, start = start, end
    return start <= n <= end


def is_divisible(dividend, divisor):
    return dividend % divisor == 0


def is_even(num):
  return num % 2 == 0


def is_odd(num):
    return num % 2 != 0


def lcm(lst):
    """最小公倍数"""
    def _lcm(x, y):
        return int(x * y / math.gcd(x, y))

    return reduce(_lcm, lst)

print("lcm", lcm([2, 3, 12, 8]))


def max_by(lst, fn):
    return max(map(fn,lst))


def median(lst):
    """序列的中位数"""
    lst.sort()
    length = len(lst)
    if length % 2 == 0:
        return (lst[length //2 - 1] + lst[length // 2]) / 2
    else:
        return lst[length // 2]

print("median", median([1, 2, 3, 4, 5]))
# median 3
print("median", median([1, 4, 6, 8]))
# median 6.0


def min_by(lst, fn):
    return min(map(fn,lst))


def sum_by(lst, fn):
    return sum(map(fn,lst))
    
