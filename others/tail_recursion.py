#
"""递归调用容易引起栈溢出
"""
import time


def fact(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return n*fact(n-1)

# 尾递归优化


def fact_tail(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    else:
        return fact_iter(num-1, num*product)


def hanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n - 1, a, c, b)
        print(a, '-->', c)
        hanoi(n - 1, b, a, c)


def main():
    print(f"start time: {time.ctime()}")
    # print(fact(100))
    print(fact_tail(100))
    print(f'end time: {time.ctime()}')


if __name__ == '__main__':
    main()
    hanoi(5, "A", 'B', 'C')
