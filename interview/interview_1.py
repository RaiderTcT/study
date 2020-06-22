# coding=utf-8
'''
@Author: Ulysses
@Description: 
@Date: 2020-02-28 15:21:56
@LastEditors: Ulysses
@LastEditTime: 2020-06-21 20:07:22
'''
"""interview"""
import threading

#%%
# 反向输出
S1 = (1, 2, 3, 4, 5, 6, 7, 8)
for i in range(len(S1)-1, -1, -1):
    x = S1[i]
    print(x)
# %%
# 删除list的重复元素
L = [1, 2, 7, 3, 4, 5, 5, 4, 6, 7, 7, 7]
print(set(L))
D = {}
for x in L:
    D[x] = 1
MY_LIST = list(D.keys())
print(MY_LIST)

#%%
def choose(_bool, a, b):
    """"and or 封装"""
    return (_bool and [a] or [b])[0]

print(choose(1, "s", 'b'))


#%%
def Singleton(cls):
    """单例模式，类装饰器"""
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton


# class Singleton1():
#     """单例模式，new方法实现"""
#     _instance_lock = threading.Lock()

#     def __init__(self):
#         pass

#     def __new__(cls, *args, **kwargs):
#         if not hasattr(Singleton1, "_instance"):
#             with Singleton1._instance_lock:
#                 if not hasattr(Singleton1, "_instance"):
#                     Singleton1._instance = object.__new__(cls)
#         return Singleton1._instance


@Singleton
class A():
    a = 1

    def __init__(self, x=0):
        self.x = x

A1 = A(1)
A2 = A(3)
print(A1.x, A2.x)
print(id(A1), id(A2))
# %%
class Single:
    __instance=None
    __first_init=False
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    def __init__(self,name):
        if not self.__first_init:
            self.name=name
            Single.__first_init=True

s1 = Single('aaa')
s2 = Single('bbb')

print(s1.name, s2.name)

# %%
a = [1, 2, 3, 4, ["a", "n"]]
b = a
b[4][1] = "c"
print(a)
print(b)

# %%
class PositiveInt(int):
    def __new__(cls, value):
        return super().__new__(cls, abs(value))

p1 = PositiveInt(-3)
p1


# %%
#6、Python实现列表去重  【并保证原来的顺序】
num_list = [1, 3, 1, 5, 3, 6, 1]
res = [num for num in set(num_list)]
print(res)

# %%
#9、生成一个16位的随机字符串
import random
import string
print(
    ''.join(
        (random.choice(string.printable) for _ in range(16))
    )
)

# %%
[random.choice(string.printable) for _ in range(16)]

# %%
#10、一句话解释什么样的语言能够用装饰器?
# 函数可以作为参数传递

# %%
#15、python 中生成随机整数、随机小数、2-6 之间小数方法？
print(random.randint(1,10))  #随机整数
print(random.random())       #随机小数
print(random.uniform(2,6))   #2-6之间的小数
#%%
#17、<div class="nam">Python</div>，用正则匹配出标签里面的内容（“Python”），其中 class 的类名是不确定的。
import re
s='<div class="nam">Python</div>'
res=re.findall(r'<div class=".*">(.*?)<.*>',s)[0]
print(res) #Python

# %%
#19、dict 中 fromkeys 的用法
keys=('info1','info2')
res=dict.fromkeys(keys,['psy',18,'girl'])
print(res)  #{'info1': ['psy', 18, 'girl'], 'info2': ['psy', 18, 'girl']}

# %%
#20、请用正则表达式输出汉字
import re
s="not 404 found 中国 2018 我爱你"
r1='[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+\s?'
res=re.sub(r1,'',s)
print(res) #中国 我爱你
# %%
l1 = [1, 2, 3, 4]
l2 = [1, 2, 3, 4]
l1 is l2


#22、列出 Python 中可变数据类型和不可变数据类型，为什么？
"""
不可变类型：int str tuple
可变类型：list dict set
原理：可变数据类型即公用一个内存空间地址，不可变数据类型即每场一个对象就会产生一个内存地址
"""
#23、dict的内部实现？
"""
在 Python 中，字典是通过哈希表实现的。也就是说，字典是一个数组，而数组的索引是键经过哈希函数处理后得到的。
哈希函数的目的是使键均匀地分布在数组中。由于不同的键可能具有相同的哈希值，即可能出现冲突，高级的哈希函数能够使冲突数目最小化。
"""
# %% 
#24、s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"？
s='ajldjlajfdljfddd'
res1=sorted(list(set(s)))  #['a', 'd', 'f', 'j', 'l']
res=''.join(res1)
print(res)  #adfjl

# %%
#27、Python 获取当前日期？
import time
import datetime
print(datetime.datetime.now()) #2019-04-03 17:06:16.347417
print(time.strftime('%Y-%m-%d %H:%M:%S'))  #2019-04-03 17:06:51

# %%
#37、a=（1，）b=(1)，c=("1") 分别是什么类型的数据？
a=(1,)
print(type(a))  #<class 'tuple'>
b=(1)
print(type(b))  #<class 'int'>
c=("1")
print(type(c))  #<class 'str'>

# %%
#37、两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]   【归并排序】
l1=[1,5,7,9]
l2=[2,2,6,8]

def merge_sort(l1,l2):
    left_p,right_p=0,0
    result=[]
    while left_p<len(l1) and right_p<len(l2):
        if l1[left_p]<l2[right_p]:
            result.append(l1[left_p])
            left_p+=1
        else:
            result.append(l2[right_p])
            right_p+=1
    result.extend(l1[left_p:])
    result.extend(l2[right_p:])
    return result
print(merge_sort(l1,l2))

# %%
#39、logging 模块的使用？
#logging是日志模块，爬虫时可能用到

import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
logger=logging.getLogger('interview_1')  #psy我设置的文件名
logger.info('Start log')
logger.debug('Do something')
logger.warning('Something maybe fail')
logger.error('Somthing exists error')
logger.critical('Break down')

# %%
#40、写一段自定义异常代码
def func():
    try:
        for i in range(5):
            if i>2:
                raise Exception('数字大于2')
    except Exception as e:
        print(e)
func() #数字大于2

# %%
#41、正则表达式匹配中，（.*）和（.*?）匹配区别？
#（.*）是贪婪匹配，会把满足正则的尽可能多的往后匹配
#（.*?）是非贪婪匹配，会把满足正则的尽可能少匹配
s = "<a>哈哈</a><a>呵呵</a>"
import re
res1 = re.findall("<a>(.*)</a>", s)
print("贪婪匹配", res1)  #贪婪匹配 ['哈哈</a><a>呵呵']
res2 = re.findall("<a>(.*?)</a>", s)
print("非贪婪匹配", res2)  #非贪婪匹配 ['哈哈', '呵呵']


# %%
#42、[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
a = [[1,2],[3,4],[5,6]]
res = [item for sub_lst in a for item in sub_lst]
print(res) 

# %%
#43、x="abc",y="def",z=["d","e","f"]，分别求出 x.join(y) 和 x.join(z) 返回的结果
#join()括号里面的是可迭代对象，x插入可迭代对象中间，形成字符串，结果一致
x="abc"
y="def"
z=["d","e","f"]
print(x.join(y))  #dabceabcf
print(x.join(z))  #dabceabcf

# %%
try:
    for i in range(5):
        pass
        # if i > 2:
        #     raise Exception('大于2')
except Exception as e:
    print(e)
else:
    # 没有捕获异常
    print('没有捕获异常, 执行else')
finally:
    print('不管是否捕获到异常，都执行finally语句')

# %%
#47、a="张明 98分"，用 re.sub，将 98 替换为 100
import re
a="张明 98分"
res=re.sub(r'\d+','100',a)
print(res)  #张明 100分

#50、提高 python 运行效率的方法
"""
（1）使用生成器，因为可以节约大量内存
（2）循环代码优化，避免过多重复代码的执行
（3）核心模块用Cython  PyPy等，提高效率
（4）多线程、多进程、协程
（5）多个if elif条件判断，可以把最有可能先发生的条件放到前面写，这样可以减少程序的判断次数，提高效率
"""
# %%
#53、两个数相除，保留两位小数
print(round(10/3,2))  #3.33

# %%
s='Date：2018/03/20'
import re
res1=re.findall('(\d+)',s)  #['2018', '03', '20']
res='-'.join(res1)
print(res)  #2018-03-20

# %%
#55、使用 pop 和 del 分别删除字典中的"name"和"age"字段，dic={"name":"zs","age":18,"sex":"girl"}
dic={"name":"zs","age":18,"sex":"girl"}
dic.pop("name")
print(dic) #{'sex': 'girl', 'age': 18}
del dic["age"]
print(dic)  #{'sex': 'girl'}


#56、简述多线程、多进程
"""
进程是资源（CPU、内存等）分配的基本单位，它是程序执行时的一个实例。
线程是程序执行时的最小单位，它是进程的一个执行流。
进程有自己的独立地址空间，每启动一个进程，系统就会为它分配地址空间，建立数据表来维护代码段、堆栈段和数据段，这种操作非诚昂贵。
【所以各个进程有自己的地址空间，彼此互相不打扰】
线程是共享进程中的数据的，使用相同的地址空间，因此CPU切换一个线程的花费比进程要小很多，同时创建一个线程的开销也比进程要小很多。
"""

"""
python提供了多种进程通信的方式，主要Queue和Pipe这两种方式，
Queue用于多个进程间实现通信，Pipe是两个进程的通信
"""
# %%
"""
IOError 输入输出异常
AttributeError 试图访问一个对象没有的属性
ImportError 无法引入模块或包，基本都是路径的问题
IndentationError 语法错误，代码没有正确的对齐
KeyError 试图访问你字典里不存在的键
SyntaxError Python代码逻辑语法出错，不能执行
NameError 使用一个还未赋予对象的变量
"""

#62、上下文管理器 with...as 的实现
# %%
class PypixOpen:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    def __enter__(self):
        self.openedFile = open(self.filename, self.mode)
        return self.openedFile
    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.openedFile.close()
        except AttributeError:
            print(exc_typ, exc_tb)
        
with PypixOpen(filename, mode) as writer:
    writer.write("Hello World from our new Context Manager!")


#63、python arg.py 1 2 命令行启动程序并传参，print(sys.argv) 会输出什么数据？
#[arg.py 1 2]

# %%
#68、对 foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4] 进行排序，将正数从小到大，负数从大到小
foo = [-5, 8, 0, 4, 9, -4, -20, -2, 8, 2, -4]
res = sorted(foo, key=lambda x: (x<0, abs(x)))
print(res)

#69、Python 传参数是传值还是传址？
# %%
"""
Python 中函数参数是引用传递（注意不是值传递）。
对于不可变类型（数值型、字符串、元组），因变量不能修改，所以运算不会影响到变量自身；
而对于可变类型（列表字典）来说，函数体运算可能会更改传入的参数变量。
"""
def func(str, lst):
    str = 'aaaa'
    lst.append(0)
    print('func: ', str, lst)
s1 = 'a'
lst = [1, 2]
func(s1, lst)  # func:  aaaa [1, 2, 0]
print(s1, lst)  # a [1, 2, 0]

# %%
#70、w、w+、r、r+、rb、rb+ 文件打开模式区别
"""
r 以只读方式打开文件。文件的指针会被放在文件的开头。这是默认模式。
w 打开一个文件只用于写入。如果该文件已存在则将其覆盖，如果该文件不存在，创建新文件。
a 打开一个文件用于追加。如果该文件存在，文件指针将会放在文件的结尾。也就是说：新的内容会被写入到已有内容之后。
                    如果该文件不存在，创建新文件进行写入。
rb 以二进制格式打开一个文件用于只读。文件指针会放在文件的开头。这是默认模式。
wb 以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
ab 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是：新的内容会被写入到已有内容之后。
                                如果该文件不存在，创建新文件进行写入。
r+ 打开一个文件用于读写。文件指针将会放在文件的开头。
w+ 打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
a+ 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会时追加模式。
                       如果该文件不存在，创建新文件进行写入。
rb+ 以二进制格式打开一个文件用于读写。文件指针会放在文件的开头。
wb+ 以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
ab+ 以二进制格式打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。
                                  如果该文件不存在，创建新文件进行写入。
"""
# %%
#71、int("1.4")、int(1.4)的输出结果？
print(int("1.4"))  #报错ValueError: invalid literal for int() with base 10: '1.4'
print(int(1.4))  #1

# %%
#73、Python 字典和 json 字符串相互转化方法  【序列化和反序列化】
import json
dic={"name":"psy","age":18}
#序列化  把python的对象编码转换为json格式的字符串
res1=json.dumps(dic)
print(res1,type(res1))  #{"age": 18, "name": "psy"} <class 'str'>     【json中一般使用""】
#反序列化 把json格式字符串解码为python数据对象。
res2=json.loads(res1)
print(res2,type(res2))  #{'name': 'psy', 'age': 18} <class 'dict'>

# %%
#74、Python 正则中 search 和 match 的区别
"""
match() 从第一个字符开始找, 如果第一个字符就不匹配就返回 None, 不继续匹配. 用于判断字符串开头或整个字符串是否匹配,速度快。 
search() 会整个字符串查找,直到找到一个匹配。
"""
import re
str1='superman'
str2='hello superman'
print(re.match('super',str1))  #<_sre.SRE_Match object; span=(0, 5), match='super'>
print(re.match('super',str1).span())  #(0, 5)
print(re.match('super',str2))  #None

print(re.search('super',str1))  #<_sre.SRE_Match object; span=(0, 5), match='super'>
print(re.search('super',str1).span())  #(0, 5)
print(re.search('super',str2))  #<_sre.SRE_Match object; span=(6, 11), match='super'>
print(re.search('super',str2).span())  #(6, 11)

# %%
#76、输入日期， 判断这一天是这一年的第几天？
import datetime
def DayOfYear():
    year=input('请输入年份：').strip()
    mon=input('请输入月份：').strip()
    day=input('请输入日：').strip()
    data1=datetime.date(year=int(year),month=int(mon),day=int(day))
    data2=datetime.date(year=int(year),month=1,day=1)
    return (data1-data2).days+1
print(DayOfYear())

# %%
#84、正则匹配以 163.com 结尾的邮箱？
email_list= ["sdgaozhe@163.com","xiaoWang@163.comheihei", ".com.602556194g@qq.com" ]
import re
pattern = re.compile('[\w]{4,20}@163\.com$')

for item in email_list:
    res = pattern.match(item)
    if res:
        print('{}符合规定的邮件地址，匹配的结果是：{}'.format(item,res.group()))
    else:
        print('{}不符合规定的邮件地址'.format(item))


# %%
#85、s="info:xiaoZhang 33 shandong",用正则切分字符串输出['info', 'xiaoZhang', '33', 'shandong']
s="info:xiaoZhang 33 shandong"
import re
res=re.split(r":| ",s)    #|表示或，根据:或 切分
print(res)  #['info', 'xiaoZhang', '33', 'shandong']



# %%
#89、阅读一下代码他们的输出结果是什么？
def multi():
    return [lambda x : i*x for i in range(4)]
print([m(2) for m in multi()])  #[6, 6, 6, 6]

def multi_1():
    return [lambda x , i=i: i*x for i in range(4)]
print([m(2) for m in multi_1()])  #[0, 2, 4, 6]


# %%
#90、代码实现 Python 的线程同步，在屏幕上依次打印10次“ABC”
from threading import Thread,Lock
mutex=Lock()
def print1(lock):
    lock.acquire()
    print('A')
    lock.release()
def print2(lock):
    lock.acquire()
    print('B')
    lock.release()
def print3(lock):
    lock.acquire()
    print('C')
    lock.release()
for i in range(10):
    t1=Thread(target=print1,args=(mutex,))
    t1.start()
    t1.join()
    t2 = Thread(target=print2, args=(mutex,))
    t2.start()
    t2.join()
    t3 = Thread(target=print3, args=(mutex,))
    t3.start()
    t3.join()

# %%
eval('123')

# %%
#98、Python 如何copy一个文件？
#  shutil 模块有一个 copyfile 函数可以实现文件拷贝  copyfile(source_file, destination_file)
from shutil import copyfile
copyfile('test.py','test_new.py')  #把该目录下的test.py复制到相同目录下的test_new.py

# %%
#105、请写出一个在函数执行后输出日志的装饰器以及计时器
"""
简单的装饰器模板：
def outter(func):
    def wrapper(*args,**kwargs):
        f=func()
    return wrapper
    
def timmer(func):  #计时器
    def wrapper(*args,**kwargs):
        start=time.time()
        func(*args,**kwargs)
        end=time.time()
        spend=round(end-start,2)
        print('该程序执行花费时间为{}'.format(spend))
    return wrapper
"""
def do_log(func):  #日志装饰器
    def wrapper(*args,**kwargs):
        if func.__name__=='debug':
            msg="debug {}".format(args[0])
        elif func.__name__=='info':
            msg="info {}".format(args[0])
        else:
            msg="{} {}".format(func.__name__,args[0])
        return func(msg,**kwargs)
    return wrapper
@do_log
def debug(msg):
    print(msg)
@do_log
def info(msg):
    print(msg)
debug('123')  #debug 123
info('456')  #info 456

# %%
#109、对列表去重并保持原来的顺序
l1=[11,2,3,22,2,4,11,3]
l2=list(set(l1))   #将列表用set去重，再转换回列表（没有按照之前的顺序）
print(l2)
l2.sort(key=l1.index)  #将上一步得到的列表排序，按照l1中的顺序排序
print(l2)  #[11, 2, 3, 22, 4]

# %%
#111、下面的输出是什么
def extend_list(v,li=[]):
    li.append(v)
    return li
list1=extend_list(10)
list2=extend_list(123,[])
list3=extend_list('a')
print(list1)  #[10,'a']
print(list2)  #[123]
print(list3)  #[10,'a']
print(list1 is list3)  #True

# %%
#113、下面代码执行完的输出
def func(m):
    for k,v in m.items():
        m[k+2]=v+2
m={1:2,3:4}
l=m  #浅拷贝
l[9]=10
func(l)  # RuntimeError: dictionary changed size during iteration
m[7]=8
print("l:",l)
print("m:",m)
#【原理！】
#     在迭代一个列表或者字典的时候，不能修改列表或字典的大小！！！！！！
# %%
#125、数据库【设计表结构（外键约束怎么建？！）】
"""设计 图书管理系统 表结构：
    - 书（pk 书名）
    - 作者（pk 姓名）
    - 出版社（pk 出版社名称 地址）
    分析：
    一本书只能由一家出版社出版      【多对一，多个出版社对应一本书】==》设置外键，外键放置在“一”的表里面，大家都可以用
    一本书可以有多个作者，一个作者也可以写多本书  【多对多】==》通过第三张表，分别与书和作者建立联系
"""
"""MySQL中建表的语句
CREATE TABLE book(
    id INT PRIMARY KEY AUTO_INCREMENT,title VARCHAR(64),publisher_id INT,
    FOREIGN KEY (publisher_id) REFERENCES publisher(id));
CREATE TABLE author(
    id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(32));
CREATE TABLE book2author(
    id INT PRIMARY KEY AUTO_INCREMENT,book_id INT,author_id INT,
    FOREIGN KEY (book_id) REFERENCES book(id),
    FOREIGN KEY (author_id) REFERENCES author(id));
CREATE TABLE publisher(
    id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(64),address VARCHAR(255));
"""
# %% python可以使用连续赋值, 从左至右.
x = [0, 1]
 
i = 0
 
i, x[i] = 1, 2
 
print(x)  # [0, 2]

# %%
"""
有两个序列a,b，大小都为n,序列元素的值任意整数，无序；要求：通过交换a,b 中的元素，使[序列a 元素的和]与[序列b 元素的和]之间的差最小。
"""
"""
当前数组a和数组b的和之差为A = sum(a) - sum(b)，a的第i个元素和b的第j个元素交换后，a和b的和之差为 A’ = sum(a) - a[i] + b[j] - （sum(b) - b[j] + a[i]) = sum(a) - sum(b) - 2 (a[i] - b[j]) = A - 2 (a[i] - b[j]) 设x = a[i] - b[j]，那么 A’ = |A - 2x|，当然A’ 越小也好，所以当x 在 (0,A)之间时，做这样的交换才能使得交换后的a和b的和之差变小，x越接近A/2效果越好,如果找不到在(0,A)之间的x，则当前的a和b就是答案。 所以算法大概如下：在a和b中寻找使得x在(0,A)之间并且最接近A/2的i和j，交换相应的i和j元素，重新计算A后，重复前面的步骤直至找不到(0,A)之间的x为止。
"""


# l1 =[random.randint(1, 100) for i in range(10)]
# l2 = list(range(10))
l1 = [100,99,98,1,2, 3]
l2 = [1, 2, 3, 4,5,40]

def change(l1, l2):
    flag = True
    n = len(l1)
    while flag:
        flag = False
        best_position = ()
        min_diff = float('inf')
        for i in range(n):
            for j in range(n):
                m = l1[i] - l2[j]
                diff_sum = abs(sum(l1) - sum(l2))
                diff_sum_2_m = abs(m - diff_sum / 2)
                if 0<m<diff_sum and diff_sum_2_m < min_diff:
                    min_diff = diff_sum_2_m
                    best_position = (i, j)
                    # l1[i], l2[j] = l2[j], l1[i]
                    flag = True
        if flag:
            i, j = best_position
            l1[i], l2[j] = l2[j], l1[i]


change(l1, l2)
print(l1)
print(l2)
print(sum(l1), sum(l2))
#%%
# 新的默认列表仅仅只在函数被定义时创建一次。随后当 extendList 没有被指定的列表参数调用的时候，其使用的是同一个列表
def extendList(val, lst=[]):
    lst.append(val)
    return lst

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')
print('l1= ', list1)
print('l2= ', list2)
print('l3= ', list3)


#%%
def extendList(val, lst=None):
    if lst is None:
        lst = []
    lst.append(val)
    return lst
list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')
print('l1= ', list1)
print('l2= ', list2)
print('l3= ', list3)
