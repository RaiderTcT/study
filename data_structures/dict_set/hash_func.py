#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Ulysses
@Date: 2019-10-16 09:23:50
@Description: 散列函数
@LastEditTime: 2019-10-17 09:32:09
'''
def str_hash(s):
    """
    非整数关键码->整数, 再使用整数散列
    把一个字符看做一个整数(字符的编码值),整个字符串视为以某个整数为基数的整数
    基数使用素数29或31
    """
    h1 = 0
    for c in s:
        h1 = h1 * 29 + ord(c)
    return h1

def int_str_hash(sn):
    """整数散列"""
    h = 0
    for c in sn:
        h = (h*10+int(c)*31) % 65521  # 除余法
    return h

if __name__ == "__main__":
    s1 = "asdfghjkl"
    s2 = "123456789"
    int_str1 = str_hash(s1)
    int_str2 = str_hash(s2)
    print(s1, int_str1, int_str_hash(str(int_str1)))
    print(s2, int_str2, int_str_hash(str(int_str2)))
    print(s2, int_str_hash(s2))
