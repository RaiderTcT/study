import functools


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


def count_1():
    fs = []
    for i in range(1, 4):
        def f():
            print(f"i = {i}")
            return i*i
        fs.append(f)
    return fs


# 闭包 返回函数不要引用任何循环变量，或者后续会发生变化的变量

def count_2():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


class partial(object):
    def __init__(self, func, **kwargs):
        self.func = func
        #self.args = args
        self.kwargs = kwargs

    def __call__(self, *args, **kwargs):
        #args = self.args + args
        return self.func(*args, **kwargs)


if __name__ == "__main__":

    # 偏函数
    int2 = functools.partial(int, base=2)
    int16 = partial(int, base=2)
    f1 = lazy_sum(1, 2, 3, 4, 5)
    print(f1())
    f1_1, f1_2, f1_3 = count_1()
    f2_1, f2_2, f2_3 = count_2()
    print(f1_1())
    print(f1_2())
    print(f1_3())
    print(f2_1())
    print(f2_2())
    print(f2_3())
    print(count_1())
    print(int16('100001010110101'))
    print(int2('100001010110101'))
