#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Ulysses
@Date: 2019-09-26 17:15:45
@Description: 使用types.FunctionType 动态创建函数
@LastEditTime: 2019-09-26 17:22:02
'''
from  types import FunctionType

s = "def foo(): return 'bar'"
code = compile(s, '', 'exec')
print(type(code))  # <class 'code'>  代码对象
# 如果代码对象表示一个函数，co_consts 中的第一项将是函数的文档字符串
func = FunctionType(code.co_consts[0], globals(), '')
print(type(func), func())
