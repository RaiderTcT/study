from threading import Timer

def hello():
    print("hello, world")

# 5s后运行hello函数
t = Timer(5, hello)
t.start()