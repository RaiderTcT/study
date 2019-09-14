#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 栈的简单应用
@Date: 2019-09-14 09:29:10
@Author: Ulysses
@LastEditTime: 2019-09-14 10:35:24
'''
from data_structures.stack_queue.stack import LStack, SStack


def reverse(lst):
    """反序"""
    st1 = SStack()
    for x in lst:
        st1.push(x)
    lst2 = []
    while not st1.is_empty():
        lst2.append(st1.pop())
    return lst2


def check_parens(text):
    """
    检查括号配对:遇到的闭括号要与最近的未匹配的开括号配对
    括号不同种类()[]{},可能重复或嵌套,保存遇到的开括号,匹配后删除
    1. 顺序扫描所有字符
    2. 跳过其他字符, 开括号入栈
    3. 遇到闭括号时,弹出栈顶开括号,若没有开括号,出现单独的闭括号,失败
    4. 匹配成功则继续,失败时检查结束
    5. 结尾时,栈中还有开括号,失败
    """
    parens = "()[]{}"
    out_parens = "([{"
    opposite = {')': "(", ']': '[', '}': '{'}

    def parentheses(text):
        """返回括号及其位置"""
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in parens:
                i += 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1

    st = SStack()
    for pr, i in parentheses(text):
        if pr in out_parens:  # 开括号入栈
            st.push((pr, i))
        elif st.is_empty():  # 单独的闭括号
            print(f"{i}位置括号{pr}配对出错,没有对应的开括号")
            return False
        elif st.pop()[0] != opposite[pr]:
            print(f"{i}位置括号{pr}配对出错,括号不匹配")
            return False
        else:
            pass
    if not st.is_empty():  # 多余开括号
        while not st.is_empty():
            pr, i = st.pop()
            print(f"{i}位置括号{pr}缺少对应的闭括号")
        return False
    print('全部配对')
    return True

if __name__ == "__main__":
    s = "(时间)[单独{fecndk(扶不上)}]"
    check_parens(s)
