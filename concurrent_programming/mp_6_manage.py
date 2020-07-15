"""
Maneger
"""
from multiprocessing import Process, Manager

def func(i, dic):
    dic['num'] = 100 + i
    print(dic.items())

if __name__ == '__main__':
    dic = Manager().dict()
    for i in range(5):
        p = Process(target=func, args=(i, dic))
        p.start()
        p.join()
