

# Create your tests here.
import time
import functools


#  参数化装饰器,
#  参数化装饰器func(tag)
# 接收参数
def tags(tag):
    def tag_decorator(func):
        #update_wrapper的装饰器形式
        # 从被装饰的函数func中提取属性attr给修饰器函数tag_decorator
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return f'<{tag}>{func(*args, **kwargs)}</{tag}>'
        return wrapper
    if callable(tag):  # 不带参数时，tag是要执行的函数的名字
        tag_decorator = tag_decorator(tag)
        print('func name:%s\n' % tag.__name__)
    return tag_decorator


def decorator(func):

    def time_count(*args, **kwargs):
        start_time = time.time()
        print('begin call\n')
        num = func(*args, **kwargs)
        end_time = time.time()
        print('end call\n')
        print(end_time-start_time)
        return num
    return time_count


# 类形式的装饰器

class P(object):
    # def __init__(self, func):
    #     self.func = func

    # def __call__(self, *args, **kwargs):
    #     print('func name:%s\n'% self.func.__name__)
    #     return self.func(*args, **kwargs)
    def __init__(self, level='func info'):
        self.level = level

    def __call__(self, func):
        def warpper(*args, **kwargs):
            print("func :%s\n" % self.level)
            return func(*args, **kwargs)
        return warpper


class Student:
    def __init__(self, score):
        self.score = score

    @decorator
    def get_score(self):
        return self.score


@tags('div')
@tags('head')
@tags
def get_upper(text):
    return text.upper()


@P('info ')
def add(*args):
    return sum(args)


if __name__ == "__main__":
    print(get_upper('nihaoa'))
    print(get_upper.__name__)
    s1 = Student(122)
    print(s1.get_score())
    print(add(1, 2, 3))
