#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Ulysses
@Date: 2019-11-06 13:42:19
@Description: file content
@LastEditTime: 2019-11-06 14:24:21
'''
import os
import re
import random


def read_json(filename=''):
    import json
    if filename!='':
        strList = filename.split(".")
        if strList[len(strList)-1].lower() == "json":
            with open(filename,mode='r',encoding="utf-8") as file:
                return json.loads(file.read())

data = read_json(r'D:\workspace\study\bullshit\data.json')
famous = data["famous"] # a 代表前面垫话，b代表后面垫话
before = data["before"] # 在名人名言前面弄点废话
after = data['after']  # 在名人名言后面弄点废话
bosh = data['bosh'] # 代表文章主要废话来源

title = "学生会退会"
repeat = 2

def shuffle(lst):
    global repeat
    pool = list(lst) * repeat
    while True:
        random.shuffle(pool)
        for item in pool:
            yield item

next_bosh = shuffle(bosh)
next_famous = shuffle(famous)

def get_famous():
    global next_famous
    ret_fa = next(next_famous)
    ret_fa = ret_fa.replace('a', random.choice(before))
    ret_fa = ret_fa.replace('b', random.choice(after))
    return ret_fa

def another_paragraph():
    xx = ". "
    xx += "\r\n"
    xx += "    "
    return xx


if __name__ == "__main__":
    xx = input("请输入文章主题:")
    for x in xx:
        tmp = str()
        while ( len(tmp) < 6000 ) :
            branch = random.randint(0,100)
            if branch < 5:
                tmp += another_paragraph()
            elif branch < 20 :
                tmp += get_famous()
            else:
                tmp += next(next_bosh)
        tmp = tmp.replace("x",xx)
        print(tmp)
