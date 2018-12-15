from dis import dis
def echo(value=None):
    print("Execution starts when 'next()' is called for the first time.")
    try:
        while True:
            try:
                value = (yield value)
            except Exception as e:
                value = e
    finally:
        print("Don't forget to clean up when 'close()' is called.")


# 返回的是iterable 对象
# 每次遇到yield关键字后返回相应结果，并保留函数当前的运行状态，等待下一次的调用
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1
    print('close')


def g(x):
    # for item in range(x, 0, -1): yield item
    yield from range(x, 0, -1)
    # yield from range(x)

def MyGenerator():
    value = (yield 1)
    value = (yield value)

def f_wrapper2(fun_iterable):
    print('start')
    yield from fun_iterable  #注意此处必须是一个可迭代对象
    print('end')
wrap = f_wrapper2(fab(5))
for i in wrap:
    print(i,end=' ')


if __name__ == "__main__":
    gen = MyGenerator()
    # send方法和next方法唯一的区别是
    # 在执行send方法会首先把上一次挂起的yield语句的返回值通过参数设定，
    # 从而实现与生成器方法的交互
    # print(gen.__next__())
    print(gen.send(None))
    print(gen.send(6))
    print(list(g(5)))
    generator = echo(5)
    print(next(generator))
    print(next(generator))
    for n in fab(10):
        print(n, end=' ')
    print('  ')
    f = fab(7)
    print(f'fabonacci: {f.__next__()}')
    # 向生成器传递参数
    # send(value)
    # The value argument becomes the result of the current yield expression
    #  When send() is called to start the generator, it must be called with None as the argument,
    #  because there is no yield expression that could receive the value.
    print(generator.send(2))
    dis(fab)
    # 在生成器暂停的地方引发指定类型的异常
    # f.throw(TypeError, 'spam')
    # Raises a GeneratorExit at the point where the generator function was paused.
    # 生成器暂停了调用， 正常退出或其他错误退出时do nothing
    f.close()
