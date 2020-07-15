from random import randrange, choice
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime, time

tlds = ('com', 'cn', 'org', 'net', 'gov')
# xrange 返回一个生成器
# range  返回一个列表
l = []
for i in range(randrange(5, 11)):
    # 取当前时间 秒 ，随机生成的时间在1970 - now
    dtint = randrange(int(time()))
    # 秒 -》 时间字符串
    dtstr = ctime(dtint)
    llen = randrange(4, 8)
    # 登陆信息 lc: 'abcdefghijklmnopqrstuvwxyz'
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)
    # 域名
    dom = ''.join(choice(lc) for j in range(dlen))
    info = dtstr + '::' + login + '@' + dom + '.' + choice(tlds) + '::' + str(dtint) + "-" + str(llen) + '-' + str(dlen) 
    print(info)
    l.append(info)
with open('redata.txt', 'w') as f:
    for line in l:
        f.write(line)
        f.write('\n')


