"""map 和 reduce
"""
from functools import reduce


def normalize(name):
    return name.title()


def prod(L):
    return reduce(lambda x, y: x*y, L)


if __name__ == "__main__":
    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(normalize, L1))
    print(L2)
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
    if prod([3, 5, 7, 9]) == 945:
        print('测试成功!')
    else:
        print('测试失败!')
