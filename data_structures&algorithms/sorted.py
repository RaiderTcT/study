"""排序
"""
from operator import itemgetter
import hello.py
a = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

if __name__ == "__main__":
    # itemgetter 用于获取对象的哪些维的数据 函数获取的不是值，而是定义了一个函数，通过该函数作用到对象上才能获取值
    print(sorted(a, key=itemgetter(0)))
    hello.hello1()