#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author: ulysses
Date: 2020-08-21 19:40:25
LastEditTime: 2020-08-21 20:31:14
LastEditors: ulysses
Description: 
'''
# get_match((5, 6, 3, 7), (4, 9, 3, 1))

# %%
from itertools import permutations


def init_set():
    ret = []
    for i in range(0, 10):
        for j in range(i+1, 10):
            for k in range(j+1, 10):
                for l in range(k+1, 10):
                    num_list = list(permutations((i, j, k, l), 4))
                    ret.extend(num_list)
    return ret

def get_match(target, source):
    la, lb = 0, 0
    for i, t in enumerate(target):
        for j, s in enumerate(source):
            if s == t:
                if i == j:
                    la += 1
                else:
                    lb += 1
                break
    return la, lb
def match_guess(target, source, a, b):
    la, lb = get_match(target, source)
    return la == a and lb == b

def remove_num(nums, guess, a, b):
    rets = []
    for num in nums:
        if match_guess(num, guess, a, b):
            rets.append(num)
    return rets

def cal_standard(target, nums):
    ab_map = {}
    abs_ = (0, 1, 2, 3, 4, 10, 11, 12, 13, 20, 21, 22, 30, 31, 40)
    for ab in abs_:
        ab_map[ab] = 0
    for num in nums:
        (a, b) = get_match(num, target)
        ab_map[a*10 +b] += 1
    ab_counts = [ab_map[ab] for ab in abs_]
    total = sum(ab_counts)
    avg = total / len(abs_)
    sd = sum([(abc - avg) ** 2 for abc in ab_counts])
    return sd

def next_guess(nums):
    min_sd = 0 
    min_set = ()
    touched = False
    for num in nums:
        sd = cal_standard(num, nums)
        if not touched or min_sd > sd:
            touched = True
            min_sd = sd
            min_set = num
    return min_set




n = input()
nums = init_set()
print(n)
for _ in range(int(n)):
    guess, AB = input().split(' ')
    guess = tuple(guess)
    a, b = int(AB[0]), int(AB[2])
    nums = remove_num(nums, guess, a, b)
    print(len(nums))
guess = next_guess(nums)
print(guess)

# %%
4815 0A0B