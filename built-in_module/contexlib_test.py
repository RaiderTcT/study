from contextlib import contextmanager, closing
from urllib.request import urlopen


class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)


class Query_new:

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


# @contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去
@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')


@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)


if __name__ == "__main__":
    with Query('Tom') as q:
        q.query()
    with create_query('Alice') as q:
        q.query()
    with tag('html'):
        print('hello')
        print("world")
    with closing(urlopen('https://www.python.org')) as page:
        for line in page:
            print(line)
