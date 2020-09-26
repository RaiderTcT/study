#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author: ulysses
Date: 2020-08-21 19:16:07
LastEditTime: 2020-08-21 20:14:13
LastEditors: ulysses
Description: 
'''
# %%
while True:
    try:
        def tansform(v):
            tmp = ''
            count_lower = 0
            for s in v:
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

        k = int(input())
        s = input()
        var_list = s.split('-')
        v0 = var_list[0]
        v = ''.join(var_list[1:])

        if len(v) <= k:
            tmp = tansform(v)
            print('-'.join([v0] + [tmp]))
        else:
            res = []
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
    except:
        break

# %%
12abc-abCABc-4aB@