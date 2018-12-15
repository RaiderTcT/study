"""字节数组bytesarray = 二进制str
    bytes([0x13, 0x34, 0x23])
"""
import struct
from struct import calcsize


def bmp_info(data):
    tmp = struct.unpack("<ccIIIIIIHH", data)
    if tmp[0] == b'B' and tmp[1] in (b'M', b'A'):
        return {
        'width': tmp[6],
        'height': tmp[7],
        'color': tmp[9]
    }
    else:
        raise TypeError('not bmp file!')


if __name__ == "__main__":
    # 0 - 127的数据对照ASCII编码
    bs = struct.pack('>hhh', 1, 2, 64)
    # h: short 2字节整型
    print(bs, struct.calcsize('>hhh'))
    # The result is a tuple even if it contains exactly one item
    s1 = struct.unpack('>hhh', bs)
    print(s1)
    # BMP格式采用小端方式存储数据，文件头的结构按顺序如下：
    # 两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
    # 一个4字节整数：表示位图大小；
    # 一个4字节整数：保留位，始终为0；
    # 一个4字节整数：实际图像的偏移量；
    # 一个4字节整数：Header的字节数；
    # 一个4字节整数：图像宽度；
    # 一个4字节整数：图像高度；
    # 一个2字节整数：始终为1；
    # 一个2字节整数：颜色数。
    s = b'\x42\x4D\x46\x55\x22\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\xE8\x03\x00\x00\xEE\x02\x00\x00\x01\x00\x18\x00'
    # with open(r'D:\study\test.bmp', 'rb') as f:
    #     d = f.read()
    #     print(type(d))
    print(len(s))
    #     Character   Byte order  Size    Alignment
    # @   native  native  native
    # =   native  standard    none
    # <   little-endian   standard    none
    # >   big-endian  standard    none
    # !   network (= big-endian)  standard    none
    bs = struct.unpack("<ccIIIIIIHH", s)
    print(bs)
    print(bmp_info(s))