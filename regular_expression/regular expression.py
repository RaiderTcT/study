import re

s = '102300'
pa = re.compile('^(\d+?)(0*)$')
t = pa.match(s)
print(t.group(1))

e1 = '<Tom Paris>'
e2 = 'mr-bob@example.com'


def is_valid_email(addr):
    pattern = re.compile(r'^<?(\w+(\.?|\s?)\w+)>?(\w+)?@(\w+)\.(\w+)$')
    if pattern.match(addr):
        return True
    else:
        return False


def name_of_email(addr):
    pattern = re.compile(r'^<?(\w+(\.?|\s?)\w+)>?\s?(\w+)?@(\w+)\.(\w+)$')
    n = pattern.match(addr)
    if n:
        return n.group(1)
    else:
        return None


if __name__ == "__main__":
    assert is_valid_email('someone@gmail.com')
    assert is_valid_email('bill.gates@microsoft.com')
    assert not is_valid_email('bob#example.com')
    assert not is_valid_email('mr-bob@example.com')
    print(name_of_email('<Tom Paris> tom@voyager.org'))
    assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
    assert name_of_email('tom@voyager.org') == 'tom'
    # (?:...) 该分组不会保存，不会用于后续的检索和应用
    m = re.findall(r'http://(\w+\.)*(\w+\.com)',
                   'http://google.com http://wwww.google.com http://doc.google.com')
    print(m)
    ma = re.findall(r'http://(?:\w+\.)*(\w+\.com)',
                    'http://google.com http://wwww.google.com http://doc.google.com')
    print(ma)
    # "(?P<name>...)" ：在模式里面用()来表示分组（命名分组）,适用于提取目标字符串中的某一些部位
    # "(?P=name)" ：引用命名分组(别名)匹配, 匹配的内容 要一致
    m = re.search(
        r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})-(?P=areacode)', '(800) 123-4567-800')
    print(m.groups())
    print(m.group('areacode'))

    m = re.sub(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})',
               '(\g<areacode>) \g<prefix>-xxxx', '(800) 123-4567')
    print(m)
    m = re.search(r'(?P<K>a)\w(c)(?P=K)', 'abcaef')
    print(m.group())

    # 转义
    print(re.escape("www.google.com"))

    # 正向前视断言，前视匹配， 零宽度正预测先行断言
    # 当扫描指针位于某个位置时，引擎会尝试匹配指针还未扫过的字符，
    # 先于指针到达该字符
    m = re.findall(r'\w+(?= van Rossum)',
                   '''
            JANE van Rossum
            Tim Pre
            Alex van Rossum
            Ray Li
        ''')
    print(m)
    # 后行断言，引擎会尝试匹配指针已扫过的字符，后于指针到达该字符
    # 零宽度正回顾后发断言
    m = re.findall(r'(?<=800-)\w+', 'abcu800-123')
    print(m)
