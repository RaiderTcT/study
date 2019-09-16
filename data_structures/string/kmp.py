#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 无回溯匹配算法 KMP算法
@Date: 2019-09-16 19:13:57
@Author: Ulysses
@LastEditTime: 2019-09-16 20:53:29
'''
"""
KMP算法核心: 匹配不回溯.如果模式串pi匹配某个tj时失败了(pi != tj), 就找到
某个特定的ki(0 <= ki < i),用模式串中的字符pki与目标串的tj进行比较.
关键: 在pi匹配失败时, 所有的pk(0 <= k <=i)都已经匹配成功 -> 目标串中tj之前的
i个字符就是模式串p的前i个字符p0 p1 ... pi-1 ->
只需要对模式串p本身的分析决定模式串前移ki
"""


def native_matching(text, pattern):
    """
    朴素串匹配算法, O(m*n)
    """
    n, m = len(text), len(pattern)
    i, j = 0, 0
    while i < m and j < n:
        if pattern[i] == text[j]:
            i, j = i + 1, j + 1
        else:  # 模式串pattern从头开始, 目标串从下一个起始字符开始匹配
            i, j = 0, j - i + 1
    if i == m:
        return j - i
    return -1


def kmp_matching(text, pattern, pnext):
    """
    O(n), kmp
    Args:
        text ([type]): 目标串
        pattern ([type]): 模式串
        pnext ([type]): 模式串某一位置失败后, 重新匹配时前移的量
    """
    i, j = 0, 0
    n, m = len(text), len(pattern)
    while i < m and j < n:
        if i == -1 or text[j] == pattern[i]:  # 检查pattern中下一字符
            i, j = i + 1, j + 1
        else:
            # i位置不匹配时, 由使用pattern[pnext[i]]位置的字符继续检查
            i = pnext[i]
    if i == m:
        return j - i


# 对于p中的每个i,都有与之对应的下标ki,与目标串无关
def get_pnext(pattern):
    """
    部分匹配表, 生成针对p中各位置i的下一检查位置表,用于kmp算法
    1. 模式串移动后,作为一个用于匹配的字符串的新位置,其前缀子串应该与匹配失败的
    字符之前的同样长度的子串相同
    2. 如果匹配在模式串的位置i失败时,而位置i的前缀子串中满足上述条件的位置不止一处,那么只能做最短移动, 将模式串移动到最近的那个满足上述条件的位置
    寻找p0...pi-1的最长相对前后缀长度 -> 最大长度表
    如果p0p1...pi-1的最长相等前后缀的长度为k(0<=k<i-1), 在pi != tj时,模式串应该
    向右移动i-k位,即把pnext[i]设置为k
    递推pnext[i+1]的情况,对于p的前i+1个序列字符,比较pi和pk,2中情况
    1)当p[k] == p[i], 那么在p[i+1]的前i+1个字符中,就有最大长度为k+1的相同前后缀
    pnext[i+1] = pnext[i] + 1 = k + 1
    2)当p[i] != p[k], 即"p[0]...p[k-1]p[k]" != "p[i-k]...p[i-1]p[i]",需要向前
    (p[0])寻找更短的相同前后缀,即在长度为k的子串p[0]...p[k-1], 中寻找
    最大相同前后缀的长度 -> pnext[k]
    """
    i, k, m = 0, -1, len(pattern)
    pnext = [-1] * m  # 初始位置取-1
    while i < m - 1:
        if k == -1 or pattern[i] == pattern[k]:
            i, k = i + 1, k + 1
            # pnext[i] = k
            # 因为pattern[i]!=t[j]匹配失败时 必定有 pattern[k]!=t[j], 需要移动
            # pnext[k]
            if pattern[k] == pattern[i]:
                pnext[i] = pnext[k]
            else:
                pnext[i] = k
        else:
            k = pnext[k]  # 要寻找更短的相同前后缀
    return pnext


if __name__ == "__main__":
    text = 'acgcctgcskjnffacgcctgccdmksd'
    pattern = 'gcctgcc'
    pnext = get_pnext(pattern)
    print(native_matching(text, pattern))
    print(kmp_matching(text, pattern, pnext))
