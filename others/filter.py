"""fliter 筛选， 接收函数和序列，根据返回结果决定保留或删除元素
"""


def is_odd(n):
    return n % 2 == 1


def is_palindrome(num):
    s = str(num)
    return s == s[::-1]  # 反转


if __name__ == "__main__":
    print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
    output = filter(is_palindrome, range(1, 1000))
    print('1~1000:', list(output))
    if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
        print('测试成功!')
    else:
        print('测试失败!')
