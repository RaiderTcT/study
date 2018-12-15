from io import StringIO, BytesIO


if __name__ == "__main__":
    f = StringIO()
    # 在内存中读取数据, 追加，第一次指针指向0，此后累加
    f.write('hello zzz\n')
    print(f.getvalue())
    f.close()
    f = StringIO("HelloHiGoodbye\n")
    f.write('abcdefghi\n')
    while True:
        s = f.readline()
        if s == '':
            break
        print(s.strip())
    print("values:%s" % f.getvalue())
    f.close()

    # 写入的是字节码
    charset = 'utf-8'
    f = BytesIO('时间似深海\n'.encode(charset))
    print(f.getvalue())
    f.close()
    fi = BytesIO(b'\xe6\x97\xb6\xe9\x97\xb4\xe4\xbc\xbc\xe6\xb7\xb1\xe6\xb5\xb7')
    print(fi.read().decode('utf-8'))
    fi.close()