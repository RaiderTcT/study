#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Description: 栈的应用:前缀 中缀 后缀 表达式
@Date: 2019-09-14 10:36:53
@Author: Ulysses
@LastEditTime: 2019-09-14 15:34:12
'''
from data_structures.stack_queue.stack import SStack, LStack


class ESStack(SStack):
    def depth(self):
        """栈的深度"""
        return len(self._stack)


def suffix_exp_evaluator(line):
    # 表达式字符串 -> 表达式
    return suf_exp_evaluator(line.split())


def suf_exp_evaluator(exp):
    """
    遇到运算对象, 保存
    遇到运算符, 根据操作元数取前面保存的运算对象或已完成的运算结果
    """
    operators = '+-*/'  # 二元运算
    st = ESStack()
    for x in exp:
        if x not in operators:
            st.push(float(x))  # 运算对象
            continue
        if st.depth() < 2:
            raise SyntaxError("缺少运算对象")
        # 取最近的2个操作对象
        a = st.pop()
        b = st.pop()

        if x == '+':
            c = a + b
        elif x == '-':
            c = b - a
        elif x == '*':
            c = b * a
        elif x == '/':
            c = b / a
        else:
            pass
        st.push(c)  # 计算结果入栈
    if st.depth() == 1:
        return st.pop()
    raise SyntaxError("需要其他操作符")


def suffix_exp():
    while True:
        try:
            line = input('输入表达式\n')
            if line == 'end':
                return
            res = suffix_exp_evaluator(line)
            print(res)
        except Exception as e:
            print("Error:", type(e), e.args)


# 中缀表达式 转换成 后缀表达式
# 扫描到运算对象, 送出作为后缀表达式的一个项
# 运算符送出 代表要进行运算,需要考虑优先级和结合性
# 当前运算符要和前一个没有运算的符号对比, 优先级高的先执行
# 括号需要配对,里面的是优先级最高的表达式
priority = {'(': 1, '+': 3, '-': 3, '*': 5, '/': 5}
infix_operators = "+-*/()"
# (1 + 2 * 3 - 1) / (2 + 1)


def trans_infix_suffix(line):
    st = SStack()  # 运算符进栈
    exp = []  # 转换后的后端表达式

    for x in tokens(line):
        if x not in infix_operators:  # 添加运算对象
            exp.append(x)
        elif st.is_empty() or x == '(':
            st.push(x)  # 括号运算符进栈, 需要比较优先级
        elif x == ')':
            while not st.is_empty() and st.top() != '(':
                exp.append(st.pop())  # 取出栈中括号内 的运算符
            if st.is_empty():
                raise SyntaxError("缺少与之配对的左括号")
            st.pop()  # 完成,左括号弹出
        else:
            # 先处理栈中优先级较高的几个
            while (not st.is_empty() and priority[st.top()] > priority[x]):
                exp.append(st.pop())  # [1, 2, 3 , *, +. -]
            st.push(x)
    while not st.is_empty():
        if st.top() == '(':
            raise SyntaxError("多余的括号")
        exp.append(st.pop())  # 剩余优先级低的符号
    return exp


def tokens(line):
    """将line中的运算符和运算对象一项项抛出"""
    i, llen = 0, len(line)
    while i < llen:
        while line[i].isspace():
            i += 1
        if i >= llen:
            break
        if line[i] in infix_operators:
            yield line[i]
            i += 1
            continue
        j = i + 1
        # 处理运算对象
        while (j < llen and not line[j].isspace()
               and line[j] not in infix_operators):
            if ((line[j] == 'e' or line[j] == 'E') and j + 1 < llen
                    and line[j + 1] == '-'):  # 负指数 1 * e-1
                j += 1
            j += 1
        yield line[i:j]
        i = j


def inffix_exp():
    while True:
        try:
            line = input('输入表达式\n')
            if line == 'end':
                return
            res = suf_exp_evaluator(trans_infix_suffix(line))
            print(res)
        except Exception as e:
            print("Error:", type(e), e.args)


if __name__ == "__main__":
    # suffix_exp()
    inffix_exp()
