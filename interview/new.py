#!/usr/bin/env python
# coding=utf-8
'''
@Author: Ulysses
@Description: 
@LastEditors: Ulysses
@LastEditTime: 2020-07-09 17:01:04
'''

def func(file_name, *args, **kwargs):
    """
    从文件中
    Args:
        file_name ([type]): 要打开的文件
    """
    with open(file_name, 'r') as file:
        for line_no, line in enumerate(file.readlines()):
            for arg in args:  # 没指定个数 出现一次即可
                if arg in line:  
                    print('第{line_no}中找到关键字{arg}'.format(
                        line_no=line_no, arg=arg))
            for key, value in kwargs.items():
                if line.count(key) >= value:
                    print('第{line_no}中找到所需出现{value}次的关键字{arg}'.format(
                        line_no=line_no, value=value, arg=key))

""" test_file内容
arg1 arg2 arg3 kw1 kw1 kw2 kw2 kw2
arg1 arg2 arg3 kw1 kw1 kw2 kw2 kw3
arg1 arg2 arg3 kw1 kw1 kw2 kw2
"""
kw_dict = {'kw1':2, 'kw2':3}
args = ('arg1', 'arg2')

func('./test_file', *args, **kw_dict)
# func('./test_file', 'arg1', 'arg2', **kw_dict)

# 结果
# 第0中找到关键字arg1
# 第0中找到关键字arg2
# 第0中找到所需出现2次的关键字kw1
# 第1中找到关键字arg1
# 第1中找到关键字arg2
# 第1中找到所需出现2次的关键字kw1
# 第2中找到关键字arg1
# 第2中找到关键字arg2
# 第2中找到所需出现2次的关键字kw1
