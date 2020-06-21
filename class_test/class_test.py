"""
类创建析构
"""
# %%
import types


class Animal(object):
    count = 0

    def __init__(self, speed):
        Animal.count += 1
        if speed is not None:
            self.run()

    def run(self):
        print('Animal is running\n')
ani_d = Animal(10)

class Dog(Animal):
    def __init__(self, speed):
        super(Dog, self).__init__(speed)

    def go(self):
        print("gogogo\n")

    def run(self):
        print('dog is running\n')

def set_age(animal, age):
    animal.age = age


dog = Dog(111)
dog.run()
# 给实例绑定方法
dog.set_age = types.MethodType(set_age, dog)
print(type(dog))
print(Animal.count)

dog.set_age(23)
# 给类绑定方法
Animal.set_age = types.MethodType(set_age, Animal)


# %%
class Timer(object):
    def run(self):
        print('time is running\n')

time = Timer()
# 类的方法调用 time.run()
Timer.run(time,)
run_twice(time)
# 动态语言


def run_twice(args):
    args.run()
    args.run()

# %%
# __开头 私有变量private
class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        return self._height * self._width

    def __len__(self):
        return 1024

s = Screen()
s.width = 1024
s.height = 768
print(f"***{len(s)}***")
print(f"******")
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

# %%
class Fib(object):
    def __init__(self, end):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b
        self.end = end

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > self.end:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

    def __getitem__(self, n):  # 类似list取下标
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
for n in Fib(1000):
    print(n, end=' ')
print()
print(Fib(1000)[9])
print(Fib(1000)[1:7])

# %%
class Book(object):
    def __new__(cls, title):
        print('__new__')
        return super(Book, cls).__new__(cls)

    def __init__(self, title):
        print("__init__")
        super(Book, self).__init__()
        self.title = title



book = Book('the End of World')
print(book.title)


# %%
# 链式调用
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __call__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__




print(Chain().status.user.timeline.list)

# 步骤：
# 1、Chain是类名，对它进行“()”运算，即调用__init__(self)(这个有讲过哦),会生成一个实例c1，c1=Chain(path='')。
# 2、对实例c1进行“.”运算，增加一个“status”属性，即调用__getattr__(self, status),返回
# 一个新实例c2,c2=Chain(path='/status')。
# 3、对实例c2进行“.”运算，增加一个“user”属性，即调用__getattr__(self, user),返回
# 一个新实例c3,c3=Chain(path='/status/user')。
# 4、对实例c3进行“.”运算，增加一个“timeline”属性，即调用__getattr__(self, timeline),返回
# 一个新实例c4,c4=Chain(path='/status/user/timeline')。
# 5、对实例c4进行“.”运算，增加一个“list”属性，即调用__getattr__(self, list),返回
# 一个新实例c5,c5=Chain(path='/status/user/timeline/list')。
# 6、对实例c5进行“回车键”运算，即调用__repr__(self)，返回c5._path,即输出'/status/user/timeline/list'。




#%%
