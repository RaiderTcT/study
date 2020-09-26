#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author: ulysses
Date: 2020-08-21 17:59:11
LastEditTime: 2020-09-10 18:48:02
LastEditors: ulysses
Description: 
'''
# %%
words = "ABCaD"
target = 'a'
count = 0

for s in words:
    if s == target:
        count += 1
print(count)
# %%
words = input()
target = input()
count = 0
print(type(words), words)
for s in words:
    if s == target:
        count += 1
print(count)
# %%
while True:
    try:
        long_str = input().lower()
        sub_str = input().lower()
         
        count = 0
        for c in long_str:
            if sub_str == str(c):
                count += 1
        print(str(count))
    except:
        break

# %%
import sys 
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))


#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        for v in values:
            ans += v
    print(ans)

# %%
k = 3
s = "12abc-abCABc-4aBA"
tmp = ''
var_list = s.split('-')
print(var_list)
v0 = var_list[0]
print(v0)
v = ''.join(var_list[1:])
print(v)

def tansform(v):
    tmp = ''
    count_lower = 0
    for i in range(len(v)):
        s = v[i]
        if s.isupper():
            count_lower += 1
        elif s.islower():
            count_lower -= 1
        else:
            pass
    if count_lower > 0:
        tmp = v.upper()
    elif count_lower < 0:
        tmp = v.lower()
    else:
        tmp = v
    return tmp

if len(v) <= k:
    tmp = tansform(v)
    print('-'.join([v0] + [tmp]))
else:
    res = []
    count_lower = 0
    for i in range(len(v)):
        s = v[i]
        if s.isupper():
            count_lower += 1
        elif s.islower():
            count_lower -= 1
        else:
            pass
        tmp += s
        
        if len(tmp) == k:
            print(count_lower, tmp)
            if count_lower > 0:
                tmp = tmp.upper()
            elif count_lower < 0:
                tmp = tmp.lower()
            else:
                tmp = tmp
            res.append(tmp)
            tmp = ''
            count_lower = 0
    tmp = tansform(v[i:])

# print(list(v[i:]))
    print('-'.join([v0] + res + [tmp]))

# %%
with open("category.txt", 'r', encoding='utf8') as f:
    s = f.read()
    print(s)
# %%
