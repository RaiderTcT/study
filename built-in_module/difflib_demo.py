#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-3-14 下午8:44
# @Author  : Ulysses
# @Email   : ulysses1171@163.com
# @Desc    :
"""
'-':包含在第一个序列行中，不包含在第二个序列行中

'+':包含在第二个序列行中，不包含在第一个序列行中

'':两个序列行一致

'?':标志两个序列行存在增量差异

'^':标志出两个序列存在的差异字符
"""
import difflib
from pprint import pprint
import sys
import argparse
import os
from datetime import datetime
text1 = """1. Beautiful is better than ugly.
2. Explicit is better than implicit.
3. Simple is better than complex.
4. Complex is better than complicated.
""".splitlines(keepends=True)  # 保留换行符


text2 = """1. Beautiful is better than ugly.
3.   Simple is better than complex.
4. Complicated is better than complex.
5. Flat is better than nested.
""".splitlines(keepends=True)

d = difflib.Differ()
result = list(d.compare(text1, text2))
# pprint(result)
# print('\n'.join(result))
# sys.stdout.writelines(result)

# 使用HtmlDiff() 生成美观的HTML文档
d = difflib.HtmlDiff()
result = d.make_file(text1, text2)
# sys.stdout.writelines(result)
# 命令行调用 python3 difflib_demo.py > diff.html

def file_mtime(path):
    # 获取文件最近一次修改时间（秒）， 转为utc datetime 形式
    t = datetime.utcfromtimestamp(os.stat(path).st_mtime)
    # ISO标准形式 YYYY-MM-DD HH:MM:SS.mmmmmm
    return t.astimezone().isoformat()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('fromfile')
    parser.add_argument('tofile')
    options = parser.parse_args()
    
    fromfile = options.fromfile
    tofile = options.tofile
    
    
    with open(fromfile) as ff:
        fromlines = ff.readlines()
    with open(tofile) as tf:
        tolines = tf.readlines()

    diff = difflib.HtmlDiff().make_file(fromlines, tolines, fromfile, tofile,
                                        charset='utf-8')
    
    sys.stdout.writelines(diff)
    
if __name__ == '__main__':
    main()
    # python3 difflib_demo.py t1.txt t2.txt >diff2.html