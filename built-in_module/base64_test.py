import base64
import re

"""
3*8 转 4*6
转换： 字符 -> ASCII码 -> 二进制 -> 所有字符合并 -> 取6位分隔 
-> 左边2位补零 -> 转为十进制 -> 取base64对照，不足4位补上 ==
base64对照 
A - Z a - z 0 - 9   +  /
0-25  26-51 52-61   62 63 
"""


def safe_base64_decode(s):
    if isinstance(s, bytes):
        s = bytes.decode(s)
    l = len(s) % 4
    while l > 0:
        l -= 1
        s = s + '='
    print(s)
    return base64.b64decode(s)


if __name__ == "__main__":
    encode_1 = base64.b64encode(b'binarystring\x10')
    encode_2 = base64.b64encode(b'binarystring')
    encode_3 = base64.b64encode(b'\x10')
    encode_4 = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
    # + / 在URL中就不能直接作为参数 ,将其变为 - _
    encode_5 = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
    de1 = base64.urlsafe_b64decode('abcd--__')
    print(encode_1)
    print(encode_2)
    print(encode_3)
    print(encode_4)
    print(encode_5)
    print(de1)
    print(safe_base64_decode(b'YWJjZA=='))
    data = '时间'.encode('utf-8')
    print(data, data.decode('utf-8'))
