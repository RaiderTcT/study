"""interview"""
import threading

# 反向输出
S1 = (1, 2, 3, 4, 5, 6, 7, 8)
for i in range(len(S1)-1, -1, -1):
    x = S1[i]
    print(x)

# 删除list的重复元素
L = [1, 2, 3, 4, 5, 5, 4, 6, 7, 7, 7]
print(set(L))
D = {}
for x in L:
    D[x] = 1
MY_LIST = list(D.keys())
print(MY_LIST)


def choose(_bool, a, b):
    """"and or 封装"""
    return (_bool and [a] or [b])[0]

print(choose(1, "s", 'b'))


def Singleton(cls):
    """单例模式，类装饰器"""
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton


class Singleton1():
    """单例模式，new方法实现"""
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton1, "_instance"):
            with Singleton1._instance_lock:
                if not hasattr(Singleton1, "_instance"):
                    Singleton1._instance = object.__new__(cls)
        return Singleton1._instance


@Singleton
class A():
    a = 1

    def __init__(self, x=0):
        self.x = x

A1 = A(1)
A2 = A(3)
print(A1.x, A2.x)
print(id(A1), id(A2))


a = [1, 2, 3, 4, ["a", "n"]]
b = a
b[4][1] = "c"
print(a)
print(b)
